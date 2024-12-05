# https://adventofcode.com/2024/day/5
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, is_correctly_ordered


def main(data: str) -> int:
    """part 1 of the puzzle """
    pages_ordering, updates = process_data(data)
    assert all(len(x)%2==1 for x in updates), "no middle page in one or more of the updates"
    result = 0
    for pag in updates:
        if is_correctly_ordered(pag, pages_ordering):
            result += pag[len(pag)//2]
    return result


def test() -> bool:
    return main(test_input) == 143


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
