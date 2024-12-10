# https://adventofcode.com/2024/day/9
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, filesystem_checksum


def compact_disk(disk: list[int | None]) -> None:
    tail = len(disk)-1
    for i in range(len(disk)):
        if disk[i] is None:
            while disk[tail] is None and tail > i:
                tail -= 1
            if tail <= i:
                return
            assert disk[tail] is not None
            disk[i], disk[tail] = disk[tail], disk[i]


def main(data: str) -> int:
    """part 1 of the puzzle """
    disk = list(process_data(data))
    compact_disk(disk)
    return filesystem_checksum(disk)


def test() -> bool:
    return main(test_input) == 1928


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
