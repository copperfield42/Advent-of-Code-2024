# https://adventofcode.com/2024/day/7
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, calculate, operator
from tqdm_recipes import progress_bar


def concat(a: int, b: int) -> int:
    return int(f"{a}{b}")


def main(data: str) -> int:
    """part 2 of the puzzle """
    result = 0
    for j, (n, val) in enumerate(progress_bar(list(process_data(data))), 1):
        if calculate(n, val, operations=(concat, operator.mul, operator.add)):
            result += n
    return result


def test() -> bool:
    return main(test_input) == 11387


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
