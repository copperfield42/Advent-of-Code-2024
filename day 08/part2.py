# https://adventofcode.com/2024/day/8
from __future__ import annotations
from typing import Iterator
from aoc_utils import test_input, get_raw_data, process_data
from aoc_recipes.grid_recipes import where2
from aoc_recipes.figuras import Recta2
from aoc_recipes import is_valid, Point
from itertools import combinations, count


def get_antinodes(recta: Recta2, map_shape: tuple[int, int]) -> Iterator[Point]:
    yield recta.ini
    for direc in [1, -1]:
        for t in count(1):
            a = recta[t*direc]
            if is_valid(a, map_shape):
                yield a
            else:
                break


def main(data: str) -> int:
    """part 2 of the puzzle """
    mapa, frequencies = process_data(data)
    antinodes: set[Point] = set()
    for frequency in frequencies:
        for antena1, antena2 in combinations(where2(mapa==frequency), 2):
            antinodes.update(get_antinodes(Recta2.from_2_points(antena1, antena2), mapa.shape))
    return len(antinodes)


def test() -> bool:
    return main(test_input) == 34


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
