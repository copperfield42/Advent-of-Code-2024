# https://adventofcode.com/2024/day/12
from __future__ import annotations

from typing import Iterator, Iterable
from aoc_recipes.grid_recipes import to_str_matrix, Matrix
from aoc_recipes.grid_recipes import flood_fill, where2, Point, vecinos
from aoc_recipes import DIRECCIONES
from collections import Counter


test_input_1 = """
AAAA
BBCD
BBCC
EEEC
"""


test_input_2 = """
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
"""


test_input_3 = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""


def extrac_regions(mapa: Matrix[str], plots: Iterable[str]) -> Iterator[tuple[str, set[Point]]]:
    for plot in plots:
        highlight: Matrix[bool] = mapa == plot
        points: set[Point] = set(where2(highlight))
        while points:
            p = points.pop()
            region_map = flood_fill(~highlight, p)
            region = set(where2(region_map))
            points.difference_update(region)
            yield plot, region


def process_data(data: str) -> tuple[set[str], Matrix[str]]:
    """transform the raw data into a processable form"""
    mapa = to_str_matrix(data)
    plots = {x for x in set(data) if x.isalpha()}
    return plots, mapa
    pass


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
