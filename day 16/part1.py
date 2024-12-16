# https://adventofcode.com/2024/day/16
from __future__ import annotations
from aoc_utils import test_input_1, test_input_2, get_raw_data, process_data
from aoc_utils import find_best_path


def main(data: str) -> int:
    """part 1 of the puzzle """
    start, target, mapa = process_data(data)
    cost, _ = find_best_path(mapa, start, target)
    return cost


def test() -> bool:
    assert main(test_input_1) == 7036, "fail example 1"
    assert main(test_input_2) == 11048, "fail example 2"
    return True


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
