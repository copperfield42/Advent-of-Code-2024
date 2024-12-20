# https://adventofcode.com/2024/day/20
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir
from aoc_recipes.grid_recipes import to_str_matrix, where2, Point, Matrix, vecinos
from aoc_recipes.graph_theory import a_star_shortest_path


test_input = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""


def neighbors(mapa: Matrix[str], pos: Point) -> Iterator[Point]:
    for v in vecinos(pos):
        if mapa[v] != "#":
            yield v


def process_data(data: str) -> tuple[Point, ...]:
    """transform the raw data into a processable form"""
    mapa = to_str_matrix(data)
    s = next(where2(mapa == "S"))
    e = next(where2(mapa == "E"))
    _, path = a_star_shortest_path(mapa, s, e, neighbors)
    return path


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
