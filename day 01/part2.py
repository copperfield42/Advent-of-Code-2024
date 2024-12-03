# https://adventofcode.com/2024/day/1
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, ir
from collections import Counter




def main(data: str) -> int:
    """part 2 of the puzzle """
    location_id, location_id2 = ir.unzip(process_data(data))
    count = Counter(location_id2)
    return sum(x*count[x] for x in location_id)


def test() -> bool:
    return main(test_input) == 31


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
