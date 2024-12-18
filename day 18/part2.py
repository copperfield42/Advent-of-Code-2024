# https://adventofcode.com/2024/day/18
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import Point, a_star_shortest_path, neighbors, MemoryMap
from tqdm_recipes import progress_bar


def main(data: str, shape: tuple[int, int] = (71, 71), sample: int = 1024) -> str:
    """part 2 of the puzzle """
    bytes_pos = list(process_data(data))
    first_sample = bytes_pos[:sample]
    pending = bytes_pos[sample:]
    memory_map = MemoryMap(shape, set(first_sample))
    start = Point(0, 0)
    goal = Point(*shape) - Point(1, 1)

    _, path = a_star_shortest_path(memory_map, start, goal, neighbors)

    for corrupted in progress_bar(pending):
        memory_map.corrupted.add(corrupted)
        if corrupted in path:
            _, path = a_star_shortest_path(memory_map, start, goal, neighbors)
        else:
            continue
        if path is None:
            break

    return ",".join(map(str, corrupted))


def test() -> bool:
    return main(test_input, (7, 7), 12) == "6,1"


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
