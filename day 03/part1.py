# https://adventofcode.com/2024/day/3
from __future__ import annotations

from aoc_utils import test_input, get_raw_data
import re
import operator


def main(data: str) -> int:
    """part 1 of the puzzle """
    return sum(eval(chunk, {"mul": operator.mul}) for chunk in re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", data))


def test() -> bool:
    return main(test_input) == 161


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
