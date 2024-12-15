# https://adventofcode.com/2024/day/15
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, test_input_2
from aoc_utils import Matrix, DIRECCIONES, Point, where2, gps


def movement(mapa: Matrix[str], vector: Point) -> None:
    """update the map by one step"""
    robot = next(where2(mapa == "@"))
    pos = robot + vector
    to_move: list[tuple[Point, str]] = [(robot, "."), (pos, "@")]
    while True:
        match mapa[pos]:
            case "@":
                raise ValueError("second robot found")
            case "O":
                pos += vector
                to_move.append((pos, "O"))
            case "#":
                return
            case ".":
                break
    for pos, item in to_move:
        mapa[pos] = item
    pass


def main(data: str) -> int:
    """part 1 of the puzzle """
    mapa, moves = process_data(data)
    for move in moves:
        movement(mapa, DIRECCIONES[move])
    return gps(mapa, "O")


def test() -> bool:
    assert main(test_input_2) == 2028, "fail small example"
    assert main(test_input) == 10092, "fail big example"
    return True


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
