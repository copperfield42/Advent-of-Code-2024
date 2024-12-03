# https://adventofcode.com/2024/day/2
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir


test_input = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


def is_safe(report: tuple[int, ...]) -> bool:
    if ir.is_sorted(report, reverse=False, strict=True) or ir.is_sorted(report, reverse=True, strict=True):
        return all(abs(a-b) <= 3 for a, b in ir.pairwise(report))
    return False


def process_data(data: str) -> Iterator[tuple[int, ...]]:
    """transform the raw data into a processable form"""
    for line in ir.interesting_lines(data):
        yield tuple(map(int, line.split()))
    pass


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
