# https://adventofcode.com/2024/day/8
from __future__ import annotations
from aoc_recipes.grid_recipes import Matrix, to_str_matrix


test_input = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""


def process_data(data: str) -> tuple[Matrix[str], set[str]]:
    """transform the raw data into a processable form"""
    return to_str_matrix(data), {f for f in data if f.isalnum()}
    pass


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()