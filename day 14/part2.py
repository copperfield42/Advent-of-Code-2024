# https://adventofcode.com/2024/day/14
from __future__ import annotations

from aoc_utils import get_raw_data, process_data
import numpy
from aoc_recipes.grid_recipes import show_bool_matrix2
import contextlib
from aoc_recipes import find_pattern_size, find_pattern
from itertools import count, combinations
from tqdm_recipes import progress_bar


def print_all_patterns(data: str, shape: tuple[int, int] = (101, 103)) -> None:
    robot_path = list(process_data(data))
    canvas = numpy.zeros(shape, dtype=bool)
    print("finding pattern")
    pattern = find_pattern_size(tuple(r[i] % shape for r in robot_path) for i in progress_bar(count()))
    with open(f"screen shot {shape}.txt", "w", encoding="utf8") as file, contextlib.redirect_stdout(file):
        for i in progress_bar(range(pattern.non_periodic + pattern.periodic), desc="printing"):
            for r in robot_path:
                canvas[r[i] % shape] = True
            print(f"time={i}")
            show_bool_matrix2(canvas)
            print()
            canvas[::, ::] = False


def main(data: str, shape: tuple[int, int] = (101, 103)) -> int:
    """part 2 of the puzzle once knowing how the answer look like"""
    robot_path = list(process_data(data))
    pattern_result = find_pattern(tuple(r[i] % shape for r in robot_path) for i in progress_bar(count()))
    pattern = pattern_result.non_periodic + pattern_result.periodic
    closeness = [(i, sum(p1.distance_t(p2) == 1 for p1, p2 in combinations(set(pos), 2))) for i, pos in enumerate(progress_bar(pattern))]
    result = max(closeness, key=lambda x: x[1])[0]
    canvas = numpy.zeros(shape, dtype=bool)
    for p in pattern[result]:
        canvas[p] = True
    show_bool_matrix2(canvas.transpose())
    return result


if __name__ == "__main__":
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  # 7383
