# https://adventofcode.com/2024/day/25
from __future__ import annotations

from typing import NamedTuple
import itertools_recipes as ir


test_input = """
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
"""


class FivePinTumblerLocks(NamedTuple):
    pin_size: int
    locks: list[tuple[int, ...]]
    keys: list[tuple[int, ...]]


def process_data(data: str) -> ...:
    """transform the raw data into a processable form"""
    schemes = list(ir.isplit(map(str.strip, data.strip().splitlines())))
    length = len(schemes[0])
    keys = []
    locks = []
    for blueprint in schemes:
        values = tuple(sum(c == "#" for c in column) for column in zip(*blueprint))
        if blueprint[0][0] == "#":
            locks.append(values)
        else:
            keys.append(values)
    return FivePinTumblerLocks(length, locks, keys)


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()


def main(data: str) -> int:
    """solution of the puzzle """
    size, locks, keys = process_data(data)
    print(f"{len(locks)=} {len(keys)=} total={len(locks)*len(keys)}")
    return sum(all(k+c <= size for k, c in zip(key, lock, strict=True)) for key, lock in ir.product(keys, locks))


def test() -> bool:
    return main(test_input) == 3


if __name__ == "__main__":
    assert test(), "fail test"
    print("pass test\n")
    part1_data = get_raw_data()
    print("solution:", main(part1_data))  #
