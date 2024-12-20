# https://adventofcode.com/2024/day/20
from __future__ import annotations
from aoc_utils import test_input, get_raw_data
from part1 import main


def test() -> bool:
    return main(test_input, 20) == 0


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data, 20))  #
