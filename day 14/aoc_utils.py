# https://adventofcode.com/2024/day/14
from __future__ import annotations

from typing import Iterator
import itertools_recipes as ir
from ast import literal_eval
from aoc_recipes import Point
from aoc_recipes.figuras import Recta2


test_input = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""


def process_data(data: str) -> Iterator[Recta2]:
    """transform the raw data into a processable form"""
    for line in ir.interesting_lines(data.replace("p=", "").replace("v=", ",")):
        p1, p2, v1, v2 = literal_eval(line)
        yield Recta2(Point(p1, p2), Point(v1, v2))
    pass


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
