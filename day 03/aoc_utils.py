# https://adventofcode.com/2024/day/3
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir


test_input = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""


def process_data(data: str) -> Iterator[str]:
    """transform the raw data into a processable form"""
    return ir.interesting_lines(data)


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
