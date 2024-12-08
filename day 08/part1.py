# https://adventofcode.com/2024/day/8
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_recipes.grid_recipes import where2
from aoc_recipes.figuras import Recta2
from aoc_recipes import is_valid
from itertools import combinations


def main(data: str) -> int:
    """part 1 of the puzzle """
    mapa, frequencies = process_data(data)
    antinodes = set()
    for frequency in frequencies:
        for antena1, antena2 in combinations(where2(mapa==frequency), 2):
            recta = Recta2.from_2_points(antena1, antena2)
            anti = antena1 + 2*recta.vector, antena2 - 2*recta.vector
            antinodes.update(a for a in anti if is_valid(a, mapa.shape))
    return len(antinodes)


def test() -> bool:
    return main(test_input) == 14


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
