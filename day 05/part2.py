# https://adventofcode.com/2024/day/5
from __future__ import annotations
from typing import Literal
from aoc_utils import test_input, get_raw_data, process_data, is_correctly_ordered
import functools


def sort_pages(printed: tuple[int, ...], rules: dict[int, set[int]]) -> list[int]:
    def comp(p1: int, p2: int) -> Literal[-1, 0, 1]:
        if after := rules.get(p1):
            if p2 in after:
                return -1
            return 1
        return 0
    return sorted(printed, key=functools.cmp_to_key(comp))


def main(data: str) -> int:
    """part 2 of the puzzle """
    pages_ordering, updates = process_data(data)
    assert all(len(x)%2==1 for x in updates), "no middle page in one or more of the updates"
    result = 0
    for pag in updates:
        if not is_correctly_ordered(pag, pages_ordering):
            new = sort_pages(pag, pages_ordering)
            result += new[len(new)//2]
    return result


def test() -> bool:
    return main(test_input) == 123


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
