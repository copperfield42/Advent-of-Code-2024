# https://adventofcode.com/2024/day/18
from __future__ import annotations

from typing import Iterator
import itertools_recipes as ir
from ast import literal_eval
from aoc_recipes import Point, vecinos, is_valid
from aoc_recipes.graph_theory import a_star_shortest_path
from dataclasses import dataclass


test_input = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
"""


@dataclass
class MemoryMap:
    shape: tuple[int, int]
    corrupted: set[Point]


def neighbors(mapa: MemoryMap, position: Point) -> Iterator[Point]:
    for new in vecinos(position):
        if is_valid(new, mapa.shape) and new not in mapa.corrupted:
            yield new


def process_data(data: str) -> Iterator[Point]:
    """transform the raw data into a processable form"""
    for line in ir.interesting_lines(data):
        yield Point(*literal_eval(line))
    pass


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
