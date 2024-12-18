# https://adventofcode.com/2024/day/18
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import ir, Point, a_star_shortest_path, neighbors, numpy


def main(data: str, shape: tuple[int, int] = (71, 71), sample: int = 1024) -> int:
    """part 1 of the puzzle """
    bytes_pos = list(ir.islice(process_data(data), sample))
    memory_map = numpy.zeros(shape, dtype=bool)
    for corrupted in bytes_pos:
        memory_map[corrupted] = True

    cost, _ = a_star_shortest_path(memory_map, Point(0, 0), Point(*shape)-Point(1, 1), neighbors, build_path=None)

    return cost


def test() -> bool:
    return main(test_input, (7, 7), 12) == 22


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
