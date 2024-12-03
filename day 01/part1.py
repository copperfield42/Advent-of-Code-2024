# https://adventofcode.com/2024/day/1
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, ir


def main(data: str) -> int:
    """part 1 of the puzzle """
    a, b = ir.unzip(process_data(data))
    return sum(abs(x-y) for x, y in zip(sorted(a), sorted(b)))


def test() -> bool:
    return main(test_input) == 11


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
