# https://adventofcode.com/2024/day/11
from __future__ import annotations

from typing import Iterator, Iterable


test_input = """
125 17
"""


def blinking_stones(stones: Iterable[int]) -> Iterator[int]:
    for stone in stones:
        if stone == 0:
            yield 1
        elif (n := len(s := str(stone))) % 2 == 0:
            yield int(s[:n//2])
            yield int(s[n//2:])
        else:
            yield 2024*stone


def compose_blinking(stones: Iterable[int], blink: int) -> Iterator[int]:
    for _ in range(blink):
        stones = blinking_stones(stones)
    return stones


def process_data(data: str) -> tuple[int, ...]:
    """transform the raw data into a processable form"""
    return tuple(map(int, data.split()))
    pass


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
