# https://adventofcode.com/2024/day/4
from __future__ import annotations

from aoc_recipes.grid_recipes import to_str_matrix as process_data, where2
from aoc_recipes import DIRECCIONES, is_valid


test_input = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
