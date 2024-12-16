# https://adventofcode.com/2024/day/16
from __future__ import annotations

from typing import Iterator, NamedTuple, Callable
import itertools_recipes as ir
from aoc_recipes.grid_recipes import to_str_matrix, where2, Matrix, Point, DIRECCIONES
from aoc_recipes.graph_theory import a_star_shortest_path



test_input_1 = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""

test_input_2 = """
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
"""


class Node(NamedTuple):
    position: Point
    vector: Point


rotate90clock = Point.from_complex(1j)
rotate90anti = Point.from_complex(-1j)


def neighbors(mapa: Matrix[str], position: Node) -> Iterator[Node]:
    pos, vector = position
    new = pos + vector
    if mapa[new] != "#":
        yield Node(new, vector)
    yield Node(pos, vector*rotate90clock)
    yield Node(pos, vector*rotate90anti)


def edge_cost(mapa: Matrix[str], position: Node, next_position: Node, cost: int) -> int:
    match position.vector.dotproduct(next_position.vector):
        case 0:
            return cost + 1000
        case 1:
            return cost + 1
        case -1:
            raise ValueError("backtraking reindeer")
        case error:
            raise ValueError("unexpecter turn")


def make_is_target(goal: Point) -> Callable[[Node], bool]:
    def is_target(pos: Node) -> bool:
        return pos.position == goal
    return is_target


def make_heuristic(goal: Point) -> Callable[[Node], int]:
    def heuristic(pos: Node) -> int:
        return pos.position.distance_t(goal)
    return heuristic


def find_best_path(mapa: Matrix[str], start: Node, target: Point) -> tuple[int, list[Node]]:
    return a_star_shortest_path(mapa, start, make_is_target(target), neighbors, edge_cost, heuristic=make_heuristic(target))


def process_data(data: str) -> tuple[Node, Point, Matrix[str]]:
    """transform the raw data into a processable form"""
    mapa = to_str_matrix(data)
    s = next(where2(mapa == "S"))
    e = next(where2(mapa == "E"))
    return Node(s, DIRECCIONES[">"]), e, mapa


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
