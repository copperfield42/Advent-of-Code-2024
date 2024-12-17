# https://adventofcode.com/2024/day/17
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data





def main(data: str) -> str:
    """part 1 of the puzzle """
    compu = process_data(data)
    result = compu.run()
    return ",".join(map(str, result))


def test() -> bool:
    return main(test_input) == "4,6,3,5,6,3,5,2,1,0"


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
