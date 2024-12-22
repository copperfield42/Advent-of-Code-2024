# https://adventofcode.com/2024/day/22
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir


test_input = """
1
10
100
2024
"""


def mix(secret: int, value: int) -> int:
    return secret ^ value


def prune(secret: int) -> int:
    return secret & 16777215
    # return secret % 16777216 # 16777216 == 2**24


def evolve_secret(secret: int) -> int:
    secret = (secret ^ (secret << 6)) & 16777215
    secret = (secret ^ (secret >> 5)) & 16777215
    return (secret ^ (secret << 11)) & 16777215
    # secret = prune(mix(secret, secret << 6))  # 2**6 = 64
    # secret = prune(mix(secret, secret >> 5))  # 2**5 = 32
    # return prune(mix(secret, secret << 11))   # 2**11 = 2048


def secret_sequence(secret: int) -> Iterator[int]:
    while True:
        yield secret
        secret = evolve_secret(secret)



def process_data(data: str) -> Iterator[int]:
    """transform the raw data into a processable form"""
    for line in ir.interesting_lines(data):
        yield int(line)
    pass


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
