# https://adventofcode.com/2024/day/24
from __future__ import annotations

from aoc_utils import test_input, test_input_2, get_raw_data, process_data, compute


def main(data: str) -> int:
    """part 1 of the puzzle """
    namespace, gates = process_data(data)
    return compute(namespace, gates)


def test() -> bool:
    assert main(test_input) == 4, "fail small example"
    assert main(test_input_2) == 2024, "fail big example"
    return True


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
