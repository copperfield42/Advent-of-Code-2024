# https://adventofcode.com/2024/day/11
from __future__ import annotations
from aoc_utils import test_input, get_raw_data, process_data, compose_blinking
from itertools_recipes import ilen


def main(data: str) -> int:
    """part 1 of the puzzle """
    return ilen(compose_blinking(process_data(data), 25))


def test() -> bool:
    return main(test_input) == 55312


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #

