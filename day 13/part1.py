# https://adventofcode.com/2024/day/13
from __future__ import annotations
from aoc_utils import test_input, get_raw_data, process_data, solve


def main(data: str) -> int:
    """part 1 of the puzzle """
    tokens = 0
    for button_a, button_b, prize in process_data(data):
        if result := solve(button_a, button_b, prize):
            a, b = result
            tokens += 3*a + b
    return tokens


def test() -> bool:
    return main(test_input) == 480


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
