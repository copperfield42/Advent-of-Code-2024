# https://adventofcode.com/2024/day/19
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir


test_input = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""


def process_data(data: str) -> tuple[tuple[str, ...], list[str]]:
    """transform the raw data into a processable form"""
    lines = ir.interesting_lines(data)
    patterns = next(lines).split(", ")
    displays = list(lines)
    return tuple(patterns), displays
    pass


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
