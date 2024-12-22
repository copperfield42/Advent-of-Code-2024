# https://adventofcode.com/2024/day/21
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import make_path, NUMERIC_KEYPAD, DIRECTIONAL_KEYPAD
from itertools import pairwise, combinations
from functools import cache


DIRECTIONAL_KEYPAD_PATHS: dict[tuple[str, str], tuple[str, ...]] = {
    (b, a): tuple(make_path(DIRECTIONAL_KEYPAD, a, b))
    for key1, key2 in combinations([key for key in DIRECTIONAL_KEYPAD if isinstance(key, str)], 2)
    for a, b in [(key1, key2), (key2, key1), (key1, key1), (key2, key2)]
}


@cache
def count_steps(key1: str, key2: str, depth: int) -> int:
    if depth < 1:
        raise ValueError(f"{depth=}")
    if depth == 1:
        return len(DIRECTIONAL_KEYPAD_PATHS[key1, key2][0])
    return min(
        sum(count_steps(a, b, depth-1) for a, b in pairwise("A"+path))
        for path in DIRECTIONAL_KEYPAD_PATHS[key1, key2]
    )


def chain_of_robots(code: str, depth: int) -> int:
    return sum(count_steps(a, b, depth) for a, b in pairwise("A"+code))


def main(data: str, num_directional_keypad: int = 25) -> int:
    """part 2 of the puzzle """
    # https://www.youtube.com/watch?v=dqzAaj589cM
    result = 0
    codes = process_data(data)
    for i, code in enumerate(codes, 1):
        rutas = list(make_path(NUMERIC_KEYPAD, code))
        steps = min(chain_of_robots(path, num_directional_keypad) for path in rutas)
        result += steps * int(code[:-1])
    return result


def test() -> bool:
    return main(test_input, 2) == 126384


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part1:", main(part2_data, 2))  #
    print("solution part2:", main(part2_data, 25))  #
    print(count_steps.cache_info())
