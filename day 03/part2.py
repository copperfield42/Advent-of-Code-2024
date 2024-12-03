# https://adventofcode.com/2024/day/3
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
import re
import operator

test_input_2 = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""


def main(data: str) -> int:
    """part 2 of the puzzle """
    result = 0
    do = True
    for instruction in re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)", data):
        match instruction:
            case "do()":
                do = True
            case "don't()":
                do = False
            case _:
                if do:
                    result += eval(instruction, {"mul": operator.mul})
    return result


def test() -> bool:
    return main(test_input_2) == 48


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
