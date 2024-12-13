# https://adventofcode.com/2024/day/13
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, solve, Point


def main(data: str) -> int:
    """part 2 of the puzzle """
    tokens = 0
    correction = Point(1, 1)*10000000000000
    for button_a, button_b, prize in process_data(data):
        if result := solve(button_a, button_b, correction + prize):
            a, b = result
            tokens += 3*a + b
    return tokens


def test() -> bool:
    return main(test_input) == 875318608908


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
