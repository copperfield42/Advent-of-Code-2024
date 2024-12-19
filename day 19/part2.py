# https://adventofcode.com/2024/day/19
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from functools import cache


@cache
def numbers_of_combinations(display: str, patterns: tuple[str]) -> int:
    if not display:
        return 1
    total = 0
    for pattern in patterns:
        if display.startswith(pattern):
            total += numbers_of_combinations(display.removeprefix(pattern), patterns)
    return total


def main(data: str) -> int:
    """part 2 of the puzzle """
    patterns, displays = process_data(data)
    return sum(numbers_of_combinations(d, patterns) for d in displays)


def test() -> bool:
    return main(test_input) == 16


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
    print(numbers_of_combinations.cache_info())
