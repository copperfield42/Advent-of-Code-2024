# https://adventofcode.com/2024/day/4
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import DIRECCIONES, is_valid, where2


COORDINATES = [
    tuple(d*n for n in range(4)) for d in DIRECCIONES["*"]
]


def main(data: str) -> int:
    """part 1 of the puzzle """
    plain = process_data(data)
    result = 0
    for x in where2(plain=="X"):
        xmas = [tuple(x+c for c in word) for word in COORDINATES]
        for coord in xmas:
            if not all(is_valid(c, plain.shape) for c in coord):
                continue
            word = "".join(plain[c] for c in coord)
            if word == "XMAS":
                result += 1
    return result


def test() -> bool:
    return main(test_input) == 18


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
