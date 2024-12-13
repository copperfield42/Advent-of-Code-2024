# https://adventofcode.com/2024/day/12
from __future__ import annotations

from aoc_utils import test_input_1, test_input_2, test_input_3, get_raw_data, process_data
from aoc_utils import extrac_regions, vecinos, Point, DIRECCIONES, Iterable
from collections_recipes import CompactRange
from aoc_recipes.figuras import Recta2, LineSegment
from itertools import combinations


test_input_4 = """
EEEEE
EXXXX
EEEEE
EXXXX
EEEEE
"""

test_input_5 = """
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
"""


def count_segments(nums: Iterable[int]) -> int:
    seg = CompactRange(nums)
    return sum(a != b for a, b in seg.to_pairs())


def calculate_sides(region: set[Point]) -> int:
    if len(region) in (1, 2):
        return 4

    perimeter = set()
    for p in region:
        perimeter.update(vecinos(p*3, direcciones=DIRECCIONES["*"]))

    for p1, p2 in combinations(region, 2):
        if p1.distance_t(p2) == 1:
            p13 = p1*3
            p23 = p2*3
            recta = Recta2(p13, (p23 - p13).normalize())
            inter = LineSegment(recta, recta.find_time(p23))
            perimeter.difference_update(inter)

    for p in region:
        p1 = p + DIRECCIONES[">"]
        p2 = p + DIRECCIONES["v"]
        p3 = p + DIRECCIONES[">v"]
        if all(x in region for x in (p1, p2, p3)):
            # is a block
            p_3 = p*3
            p1_3 = p1*3
            p2_3 = p2*3
            p3_3 = p3*3

            recta1 = Recta2(p_3, (p3_3 - p_3).normalize())
            inter1 = LineSegment(recta1, recta1.find_time(p3_3))

            recta2 = Recta2(p1_3, (p2_3 - p1_3).normalize())
            inter2 = LineSegment(recta2, recta2.find_time(p2_3))

            perimeter.difference_update(inter1)
            perimeter.difference_update(inter2)

    Xs = {p.x for p in perimeter}
    Ys = {p.y for p in perimeter}
    sides = 0

    for x in Xs:
        sides += count_segments(p.y for p in perimeter if p.x == x)

    for y in Ys:
        sides += count_segments(p.x for p in perimeter if p.y == y)

    return sides


def main(data: str) -> int:
    """part 2 of the puzzle """
    plots, mapa = process_data(data)
    result = 0
    for plot, region in extrac_regions(mapa, plots):
        sides = calculate_sides(region)
        result += len(region)*sides
    return result


def test() -> bool:
    assert main(test_input_1) == 80, "fail example 1"
    assert main(test_input_2) == 436, "fail example 2"
    assert main(test_input_4) == 236, "fail example 4"
    assert main(test_input_5) == 368, "fail example 5"
    assert main(test_input_3) == 1206, "fail example 3"
    return True


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
