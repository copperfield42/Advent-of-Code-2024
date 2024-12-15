# https://adventofcode.com/2024/day/15
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import Matrix, DIRECCIONES, Point, where2, gps

test_input_3 = """
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
"""


def movement_wider(mapa: Matrix[str], move: str) -> None:
    """update the map by one step"""
    robot = next(where2(mapa == "@"))
    vector = DIRECCIONES[move]
    pos = robot + vector
    to_move: list[tuple[Point, Point, str]] = [(robot, pos, "@")]  # (old pos, new pos, item)
    pending_move: list[Point] = [pos]
    while pending_move:
        pos = pending_move.pop()
        match mapa[pos]:
            case "@":
                raise ValueError("second robot found")
            case "#":
                return
            case ".":
                continue
            case "[":
                match move:
                    case "<":
                        raise ValueError(f"bad configuration [ < at {pos}")
                    case ">":
                        pos2 = pos + vector
                        pos3 = pos2 + vector
                        assert mapa[pos2] == "]"
                        to_move += [(pos, pos2, "["), (pos2, pos3, "]")]
                        pending_move.append(pos3)
                    case "^" | "v":
                        pos2 = pos + DIRECCIONES[">"]
                        assert mapa[pos2] == "]"
                        to_move += [(pos, pos+vector, "["), (pos2, pos2+vector, "]")]
                        pending_move += [pos+vector, pos2+vector]
            case "]":
                match move:
                    case ">":
                        raise ValueError(f"bad configuration > ] at {pos}")
                    case "<":
                        pos2 = pos + vector
                        pos3 = pos2 + vector
                        assert mapa[pos2] == "["
                        to_move += [(pos2, pos3, "["), (pos, pos2, "]")]
                        pending_move.append(pos3)
                    case "v" | "^":
                        pos2 = pos + DIRECCIONES["<"]
                        assert mapa[pos2] == "["
                        to_move += [(pos2, pos2+vector, "["), (pos, pos+vector, "]")]
                        pending_move += [pos+vector, pos2+vector]
    for old, new, item in reversed(to_move):
        if mapa[old] == item:
            mapa[old] = "."
        mapa[new] = item
    pass


def main(data: str) -> int:
    """part 2 of the puzzle """
    data = data.replace("#", "##").replace("O", "[]").replace(".","..").replace("@","@.")
    mapa, moves = process_data(data)
    for move in moves:
        movement_wider(mapa, move)
    return gps(mapa, "[")


def test() -> bool:
    return main(test_input) == 9021


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
