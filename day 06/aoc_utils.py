# https://adventofcode.com/2024/day/6
from __future__ import annotations
from aoc_recipes.grid_recipes import Matrix, to_str_matrix, where2
from aoc_recipes import DIRECCIONES, Point, is_valid


test_input = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


def guard_walk(start: Point, mapa: Matrix[str]) -> bool:
    """
    mark in the Matrix mapa the position the guard walk into with a 'x'
    and return a boolean indicated if the walk is a loop or not
    """
    vector = DIRECCIONES["^"]
    position = start
    rotate90 = -1j
    seen: set[tuple[Point, Point]] = set()
    while True:
        mapa[position] = "x"
        if (position, vector) in seen:
            return True
        else:
            seen.add((position, vector))
        next_step = position + vector
        if not is_valid(next_step, mapa.shape):
            return False
        match mapa[next_step]:
            case "." | "x":
                position = next_step
            case "#" | "O":
                vector *= rotate90


def process_data(data: str) -> tuple[Point, Matrix[str]]:
    """transform the raw data into a processable form"""
    mapa = to_str_matrix(data)
    initial = next(where2(mapa=="^"))
    mapa[initial] = "."
    return initial, mapa
    pass


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
