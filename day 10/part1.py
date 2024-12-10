# https://adventofcode.com/2024/day/10
from __future__ import annotations
from aoc_utils import test_input, get_raw_data, process_data, ir, neighbors
from aoc_recipes.grid_recipes import Point, where2
from aoc_recipes.graph_theory import a_star_shortest_path


def main(data: str) -> int:
    """part 1 of the puzzle """
    mapa = process_data(data)
    result = 0
    top: Point
    bottom: Point
    for top, bottom in ir.product(where2(mapa==9), where2(mapa==0)):
        if top.distance_t(bottom) > 9:
            continue
        cost, path = a_star_shortest_path(mapa, top, bottom, neighbors)
        if path:
            result += 1
    return result


def test() -> bool:
    return main(test_input) == 36


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
