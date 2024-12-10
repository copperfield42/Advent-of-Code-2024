# https://adventofcode.com/2024/day/10
from __future__ import annotations

from typing import Iterator
import itertools_recipes as ir
from aoc_recipes.grid_recipes import Matrix, to_int_matrix as process_data
from aoc_recipes.grid_recipes import Point, Matrix, is_valid, vecinos


test_input = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""


def neighbors(grafo: Matrix[int], position: Point) -> Iterator[Point]:
    value = grafo[position]
    for veci in vecinos(position):
        if is_valid(veci, grafo.shape):
            if grafo[veci] == value-1:
                yield veci


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
