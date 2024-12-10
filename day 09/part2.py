# https://adventofcode.com/2024/day/9
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, filesystem_checksum, ir
from tqdm_recipes import progress_bar


def compact_disk_no_fragmentation(disk: list[tuple[int | None, int]]) -> None:
    for file_id in progress_bar((range(max(fid for fid, _ in disk if fid is not None)+1)[::-1])):
        pos = next(i for i, (f, _) in enumerate(disk) if f == file_id)
        file = disk[pos]
        size = file[1]
        for node_pos in range(pos):
            node = disk[node_pos]
            if node[0] is None and node[1] >= size:
                break
        else:  # no break
            continue
        free = node[1] - size
        disk[pos] = (None, size)
        disk[node_pos] = file
        if free:
            disk.insert(node_pos+1, (None, free))
        disk[:] = (next(value) if key is not None else (None, sum(v[1] for v in value)) for key, value in ir.groupby(disk, key=lambda x:x[0]))


def main(data: str) -> int:
    """part 2 of the puzzle """
    disk = [(k, ir.ilen(v)) for k, v in ir.groupby(process_data(data))]
    compact_disk_no_fragmentation(disk)
    return filesystem_checksum(ir.chain.from_iterable(ir.starmap(ir.repeat, disk)))


def test() -> bool:
    return main(test_input) == 2858


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
