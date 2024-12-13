# https://adventofcode.com/2024/day/13
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir
from aoc_recipes import Point
from ast import literal_eval
from fractions import Fraction
import poly

test_input = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""


def solve(button_a: Point, button_b: Point, goal: Point) -> tuple[int, int] | None:
    B = poly.X
    A = (goal.x - button_b.x * B) // button_a.x
    Pb = button_a.y*A + button_b.y*B - goal.y
    B_val: Fraction = poly.linear_root(Pb)
    A_val: Fraction = A(B_val)
    if A_val.denominator == 1 and B_val.denominator == 1:
        return A_val.numerator, B_val.numerator


def chain_replace(text: str, changes: Iterable[tuple[str, str]]) -> str:
    for old, new in changes:
        text = text.replace(old, new)
    return text


def process_data(data: str) -> Iterator[tuple[Point, Point, Point]]:
    """transform the raw data into a processable form"""
    changes = [("Button A: ", ""), ("Button B: ", ""), ("Prize: ", ""), ("X", ""), ("Y", ""), ("=", "")]
    for line in ir.isplit(chain_replace(data, changes).splitlines()):
        yield tuple(Point(*literal_eval(x)) for x in line)
    pass


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
