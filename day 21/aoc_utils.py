# https://adventofcode.com/2024/day/21
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir
from aoc_recipes import DIRECCIONES, Point, make_mirror_dict
from aoc_recipes.grid_recipes import vecinos
from aoc_recipes.graph_theory import find_all_best_paths
from itertools import pairwise

type KeyPad = dict[str, Point] | dict[Point, str]

test_input = """
029A
980A
179A
456A
379A
"""

"""
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+
"""

numeric_keypad_coord = {
    "A": Point(0, 0),
    "0": Point(0, 0) + DIRECCIONES["<"],

    "3": Point(0, 0) + DIRECCIONES["^"],
    "2": Point(0, 0) + DIRECCIONES["<^"],
    "1": Point(0, 0) + DIRECCIONES["<^"] + DIRECCIONES["<"],

    "6": Point(0, 0) + 2*DIRECCIONES["^"],
    "5": Point(0, 0) + 2*DIRECCIONES["^"] + DIRECCIONES["<"],
    "4": Point(0, 0) + 2*DIRECCIONES["^"] + 2*DIRECCIONES["<"],

    "9": Point(0, 0) + 3*DIRECCIONES["^"],
    "8": Point(0, 0) + 3*DIRECCIONES["^"] + DIRECCIONES["<"],
    "7": Point(0, 0) + 3*DIRECCIONES["^"] + 2*DIRECCIONES["<"],
}

NUMERIC_KEYPAD: KeyPad = make_mirror_dict(numeric_keypad_coord.items())

"""
    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
"""

directional_keypad_coord = {
    "A": Point(0, 0),
    "^": Point(0, 0) + DIRECCIONES["<"],

    ">": Point(0, 0) + DIRECCIONES["v"],
    "v": Point(0, 0) + DIRECCIONES["<v"],
    "<": Point(0, 0) + DIRECCIONES["<v"] + DIRECCIONES["<"],
}

DIRECTIONAL_KEYPAD = make_mirror_dict(directional_keypad_coord.items())

MOVES = make_mirror_dict((m,DIRECCIONES[m]) for m in "<>v^")


def neighbors(keypad: KeyPad, pos: Point) -> Iterator[Point]:
    for new in vecinos(pos):
        if new in keypad:
            yield new


def make_path(keypad: KeyPad, code: str, start: str = "A", path=()) -> Iterator[str]:
    if not code:
        yield "A".join(path+("",))
        return
    key = code[0]
    _, sub_paths = find_all_best_paths(keypad, keypad[start], keypad[key], neighbors)
    for sub in sub_paths:
        yield from make_path(keypad, code[1:], key, path+("".join((MOVES[b-a] for a, b in pairwise(sub))),))


def process_data(data: str) -> tuple[str, ...]:
    """transform the raw data into a processable form"""
    return tuple(ir.interesting_lines(data))


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
