# https://adventofcode.com/2024/day/10
from __future__ import annotations
from typing import Iterator
from aoc_utils import test_input, get_raw_data, process_data, Point, neighbors, ir
from aoc_recipes.graph_theory import a_star_shortest_path
from aoc_recipes.grid_recipes import where2, Matrix


def find_all_paths[Path: tuple[Point, ...]](mapa: Matrix[int], start: Point, goal: Point, seen: set[Path] = None) -> Iterator[Path]:
    def path_cost(graph, path: Path, node, old_cost: int) -> int | float:
        if path in seen:
            return float("inf")
        return old_cost+1

    def vecinos(graph: Matrix[int], path: Path) -> Iterator[Path]:
        for p in neighbors(graph, path[-1]):
            if p not in path:
                yield path+(p,)

    def is_target(path: Path) -> bool:
        return path[-1] == goal and path not in seen

    if seen:
        yield from seen
    else:
        seen = set()
    while True:
        cost, result = a_star_shortest_path(mapa, (start,), is_target, vecinos, path_cost)
        if result is None:
            break
        yield result[-1]
        seen.add(result[-1])
    pass


def main(data: str) -> int:
    """part 2 of the puzzle """
    mapa = process_data(data)
    result = 0
    top: Point
    bottom: Point
    for top, bottom in ir.product(where2(mapa==9), where2(mapa==0)):
        if top.distance_t(bottom) > 9:
            continue
        cost, path = a_star_shortest_path(mapa, top, bottom, neighbors)
        if path:
            result += ir.ilen(find_all_paths(mapa, top, bottom, {tuple(path)}))
    return result


def test() -> bool:
    return main(test_input) == 81


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
