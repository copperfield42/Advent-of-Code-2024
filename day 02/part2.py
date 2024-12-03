# https://adventofcode.com/2024/day/2
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, is_safe, ir


def problem_dampener(report: tuple[int, ...]) -> tuple[int, ...] | None:
    for i in range(len(report)):
        new = tuple(e for j, e in enumerate(report) if j != i)
        if is_safe(new):
            return new


def main(data: str) -> int:
    """part 2 of the puzzle """
    result = 0
    for report in process_data(data):
        if is_safe(report):
            result += 1
        else:
            if problem_dampener(report):
                result += 1
    return result


def test() -> bool:
    return main(test_input) == 4


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
