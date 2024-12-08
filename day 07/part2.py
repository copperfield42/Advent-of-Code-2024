# https://adventofcode.com/2024/day/7
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import operator, Success, is_possible_mul, is_reachable2
from tqdm_recipes import progress_bar


def concat(a: int, b: int) -> int:
    return int(f"{a}{b}")


def is_possible_concat(goal: int, num: int) -> int | None:
    new, mod = divmod(goal, 10**len(f"{num}"))
    if mod == num:
        return new


def main(data: str) -> int:
    """part 2 of the puzzle """
    result = 0
    op = (is_possible_concat, is_possible_mul, operator.sub)
    for n, val in process_data(data):
        try:
            is_reachable2(n, val, reverse_operations=op)
        except Success:
            result += n
    return result


def test() -> bool:
    return main(test_input) == 11387


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
