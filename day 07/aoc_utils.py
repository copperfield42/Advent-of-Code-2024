# https://adventofcode.com/2024/day/7
from __future__ import annotations

from typing import Iterator, Callable
import itertools_recipes as ir
import operator

test_input = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""


class Success(Exception):
    pass


def is_reachable(goal: int, numbers: tuple[int, ...], accumulated: int = None, *, operations: tuple[Callable[[int, int], int], ...]) -> bool:
    if not numbers:
        if accumulated is None:
            return False
        if goal == accumulated:
            raise Success
        else:
            return False
    if accumulated is None:
        return is_reachable(goal, numbers[1:], numbers[0], operations=operations)
    if accumulated > goal:
        return False
    n = numbers[0]
    ns = numbers[1:]
    for operation in operations:
        is_reachable(goal, ns, operation(accumulated, n), operations=operations)
    return False


def calculate(goal: int, nums: tuple[int, ...], operations: tuple[Callable[[int, int], int], ...] = (operator.mul, operator.add)) -> bool:
    try:
        is_reachable(goal, nums, operations=operations)
    except Success:
        return True
    return False


def is_reachable2(goal: int, numbers: tuple[int, ...], *, reverse_operations: tuple[Callable[[int, int], int | None], ...]) -> bool:
    """reverse check, thanks to comments in r/adventofcode"""
    if goal < 1 or not numbers:
        return False
    if len(numbers) == 1:
        if goal == numbers[0]:
            raise Success
        else:
            return False
    n = numbers[-1]
    ns = numbers[:-1]
    for operation in reverse_operations:
        if (new_goal := operation(goal, n)) is not None:
            is_reachable2(new_goal, ns, reverse_operations=reverse_operations)
    return False


def is_possible_mul(goal: int, num: int) -> int | None:
    new, mod = divmod(goal, num)
    if not mod:
        return new


def calculate2(goal: int, numbers: tuple[int, ...]) -> bool:
    try:
        is_reachable2(goal, numbers, reverse_operations=(is_possible_mul, operator.sub))
    except Success:
        return True
    return False


def process_data(data: str) -> Iterator[tuple[int, tuple[int, ...]]]:
    """transform the raw data into a processable form"""
    for line in ir.interesting_lines(data):
        test_value, *numbers = map(int, line.replace(":", "").split())
        assert test_value > 0 and all(x > 0 for x in numbers)
        yield test_value, tuple(numbers)
    pass


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
