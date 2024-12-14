# https://adventofcode.com/2024/day/14
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
import numpy
from aoc_recipes.grid_recipes import show_bool_matrix2
import contextlib_recipes
from aoc_recipes import find_pattern_size
from itertools import count
from tqdm_recipes import progress_bar


def print_all_patterns(data: str, shape: tuple[int, int] = (101, 103)) -> None:
    """part 2 of the puzzle """
    robot_path = list(process_data(data))
    canvas = numpy.zeros(shape, dtype=bool)
    print("finding pattern")
    pattern = find_pattern_size(tuple(r[i] % shape for r in robot_path) for i in progress_bar(count()))
    with open(f"screen shot {shape}.txt", "w", encoding="utf8") as file, contextlib_recipes.redirect_stdout(file):
        for i in progress_bar(range(pattern.non_periodic + pattern.periodic)):
            for r in robot_path:
                canvas[r[i]%shape] = True
            print(f"time={i}")
            show_bool_matrix2(canvas)
            print()
            canvas[::,::]=False


if __name__ == "__main__":
    print_all_patterns(get_raw_data())  # 7383
