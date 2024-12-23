# https://adventofcode.com/2024/day/23
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from itertools import combinations,permutations
from tqdm_recipes import progress_bar
import math


def main(data: str) -> int:
    """part 1 of the puzzle """
    connections = process_data(data)
    triplets: set[frozenset[str]] = set()
    for tri in progress_bar(combinations(connections, 3), desc="calculating triplets", total=math.comb(len(connections), 3)):
        if all(c1 in connections[c2] and c1 in connections[c3] for c1, c2, c3 in permutations(tri)):
            triplets.add(frozenset(tri))
    t_compu = frozenset(c for c in connections if c.startswith("t"))
    return sum(bool(t_compu & tri) for tri in triplets)


def test() -> bool:
    return main(test_input) == 7


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
