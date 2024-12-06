# https://adventofcode.com/2024/day/6
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, guard_walk, where2
import tqdm_recipes


def main(data: str) -> int:
    """part 2 of the puzzle """
    initial, mapa = process_data(data)
    walked_mapa, looped = guard_walk(initial, mapa)
    assert not looped, "already is a loop"
    candidates = set(where2(walked_mapa=="x"))
    candidates.discard(initial)
    result = 0
    for new_obstacle in tqdm_recipes.progress_bar(candidates):
        walked_mapa[(walked_mapa == "x") | (walked_mapa == "O")] = "."
        walked_mapa[new_obstacle] = "O"
        walked_mapa, looped = guard_walk(initial, walked_mapa)
        if looped:
            result += 1
    return result


def test() -> bool:
    return main(test_input) == 6


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
