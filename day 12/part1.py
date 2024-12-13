# https://adventofcode.com/2024/day/12
from __future__ import annotations
from aoc_utils import test_input_1, test_input_2, test_input_3, get_raw_data, process_data
from aoc_utils import extrac_regions, DIRECCIONES, Counter, Point, vecinos
from fractions import Fraction

PERIMETER_DIRECTION = tuple(p*Fraction(1, 2) for p in DIRECCIONES["+"])


def calculate_perimeter(region: set[Point]) -> int:
    perimeter = Counter()
    for p in region:
        perimeter.update(vecinos(p, direcciones=PERIMETER_DIRECTION))
    return len({p for p, n in perimeter.items() if n == 1})


def main(data: str) -> int:
    """part 1 of the puzzle """
    plots, mapa = process_data(data)
    result = 0
    for plot, region in extrac_regions(mapa, plots):
        peri = calculate_perimeter(region)
        result += len(region)*peri
    return result


def test() -> bool:
    assert main(test_input_1) == 140, "fail example 1"
    assert main(test_input_2) == 772, "fail example 2"
    assert main(test_input_3) == 1930, "fail example 3"
    return True


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
