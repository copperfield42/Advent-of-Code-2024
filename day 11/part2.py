# https://adventofcode.com/2024/day/11
from __future__ import annotations
from aoc_utils import get_raw_data, process_data, test_input
from functools import cache


@cache
def blinking_stone(stone: int) -> int | tuple[int, int]:
    if stone == 0:
        return 1
    elif (n := len(s := str(stone))) % 2 == 0:
        return int(s[:n//2]), int(s[n//2:])
    else:
        return 2024*stone


@cache
def number_stones(stone: int, deep: int):
    if deep < 1:
        return 1
    b = blinking_stone(stone)
    if isinstance(b, tuple):
        return number_stones(b[0], deep-1) + number_stones(b[1], deep-1)
    else:
        return number_stones(b, deep-1)


def main(data: str, times: int = 75) -> int:
    """part 1 of the puzzle """
    return sum(number_stones(stone, times) for stone in process_data(data))


def test() -> bool:
    return main(test_input, 25) == 55312


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
    print(f"{number_stones.cache_info()=}\n{blinking_stone.cache_info()=}")

