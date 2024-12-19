# https://adventofcode.com/2024/day/19
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from functools import cache


@cache
def is_valid_display(display: str, patterns: tuple[str]) -> bool:
    if not display:
        return True
    for pattern in patterns:
        if display.startswith(pattern):
            if is_valid_display(display.removeprefix(pattern), patterns):
                return True
    return False


def main(data: str) -> int:
    """part 1 of the puzzle """
    patterns, displays = process_data(data)
    return sum(is_valid_display(d, patterns) for d in displays)


def test() -> bool:
    return main(test_input) == 6


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
    print(is_valid_display.cache_info())
