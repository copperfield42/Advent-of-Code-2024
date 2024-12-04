# https://adventofcode.com/2024/day/4
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import DIRECCIONES, where2, is_valid

DIAGONALS = "<^", "<v", ">^", ">v"

COORDINATES = {
    k: DIRECCIONES[k[0]] + DIRECCIONES[k[1]] for k in DIAGONALS
}

XMAS = {"MAS", "SAM"}


def main(data: str) -> int:
    """part 2 of the puzzle """
    plain = process_data(data)
    result = 0
    for a in where2(plain=="A"):
        coord_mas1 = a + COORDINATES["<^"], a, a + COORDINATES[">v"]
        coord_mas2 = a + COORDINATES["<v"], a, a + COORDINATES[">^"]
        if not all(is_valid(c, plain.shape) for c in (coord_mas1 + coord_mas2)):
            continue
        mas1 = "".join(plain[c] for c in coord_mas1)
        mas2 = "".join(plain[c] for c in coord_mas2)
        if mas1 in XMAS and mas2 in XMAS:
            result += 1
    return result


def test() -> bool:
    return main(test_input) == 9


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
