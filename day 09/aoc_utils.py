# https://adventofcode.com/2024/day/9
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir


test_input = """
2333133121414131402
"""


def filesystem_checksum(file_system: Iterable[int | None]) -> int:
    return sum(pos*file_id for pos, file_id in enumerate(file_system) if file_id is not None)


def process_data(data: str) -> Iterator[int | None]:
    """transform the raw data into a processable form"""
    file_id = 0
    for tipo, size in zip(ir.chain.from_iterable(ir.repeat((True, False))), map(int, data.strip())):
        if tipo:
            yield from ir.repeat(file_id, size)
            file_id += 1
        else:
            yield from ir.repeat(None, size)


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
