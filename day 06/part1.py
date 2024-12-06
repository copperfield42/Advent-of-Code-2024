# https://adventofcode.com/2024/day/6
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, guard_walk


def main(data: str) -> int:
    """part 1 of the puzzle """
    initial, mapa = process_data(data)
    guard_walk(initial, mapa)
    return (mapa == "x").sum()


def test() -> bool:
    return main(test_input) == 41


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
