# https://adventofcode.com/2024/day/20
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, Point
from itertools import combinations
from collections import Counter
from tqdm_recipes import progress_bar
import math


def main(data: str, cheat_time: int = 2) -> int:
    """part 1 of the puzzle """
    if cheat_time >= 2:
        cheat_time += 1
    else:
        raise ValueError("cheat time must be 2 or more")
    path = process_data(data)
    index: dict[Point, int] = dict((p, i) for i, p in enumerate(path))
    ahorro = Counter()
    a: Point
    b: Point
    for a, b in progress_bar(combinations(path, 2), total=math.comb(len(path), 2)):
        if (len_diff := a.distance_t(b)) < cheat_time < (index_diff := abs(index[a] - index[b])):
           ahorro[index_diff-len_diff] += 1
    return sum(n for save, n in ahorro.items() if save >= 100)


def test() -> bool:
    return main(test_input) == 0


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
