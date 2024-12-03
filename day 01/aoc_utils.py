# https://adventofcode.com/2024/day/1
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir


test_input = """
3   4
4   3
2   5
1   3
3   9
3   3
"""


def process_data(data: str) -> Iterator[tuple[int, int]]:
    """transform the raw data into a processable form"""
    for line in ir.interesting_lines(data):
        yield tuple(map(int, line.split()))
    pass


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
