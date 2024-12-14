# https://adventofcode.com/2024/day/14
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from collections import Counter
from math import prod


def cuadrantes(x: int, y: int) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    dx, mx = divmod(x, 2)
    qx = (0, dx), (dx+mx, x)
    dy, my = divmod(y, 2)
    qy = (0, dy), (dy+my, y)
    return [(px, py) for px in qx for py in qy]


def main(data: str, shape: tuple[int, int] = (101, 103)) -> int:
    """part 1 of the puzzle """
    post_at_time100 = Counter(r[100] % shape for r in process_data(data))
    robot_per_cuadrante = {c: 0 for c in cuadrantes(*shape)}
    for pos, count in post_at_time100.items():
        for cua in robot_per_cuadrante:
            x, y = pos
            (x1, x2), (y1, y2) = cua
            if x1 <= x < x2 and y1 <= y < y2:
                robot_per_cuadrante[cua] += count
    return prod(robot_per_cuadrante.values())


def test() -> bool:
    return main(test_input, (11, 7)) == 12


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
