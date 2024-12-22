# https://adventofcode.com/2024/day/22
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import secret_sequence
from itertools_recipes import nth


def main(data: str) -> int:
    """part 1 of the puzzle """
    return sum(nth(secret_sequence(num), 2000) for num in process_data(data))


def test() -> bool:
    return main(test_input) == 37327623


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
