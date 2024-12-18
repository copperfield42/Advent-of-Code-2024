# https://adventofcode.com/2024/day/17
from __future__ import annotations

from aoc_utils import get_raw_data, process_data, ChronospatialComputer
from tqdm_recipes import progress_bar
from itertools_recipes import chunked

test_input_2 = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""


def find(compu: ChronospatialComputer, program: tuple[int, ...], ans: int = 0) -> int:
    """https://www.youtube.com/watch?v=y-UPxMAh2N8"""
    if not program:
        return ans
    for t in range(8):
        a = ans << 3 | t
        compu.setup(a)
        output = compu.run()
        if output[0] == program[-1]:
            sub_ans = find(compu, program[:-1], a)
            if sub_ans is None:
                continue
            return sub_ans


def main(data: str) -> int:
    """part 2 of the puzzle """
    compu = process_data(data)
    program = compu.program
    test_program = program[:-2]

    assert program[-2:] == (3, 0), "program doesn't end with JNZ 0"
    assert not any(operand != 3 for opcode, operand in chunked(program, 2) if opcode == 0), "program include ADV with a operand other than 3"
    assert sum(operand == 3 for opcode, operand in chunked(program, 2) if opcode == 0) == 1, "program include multiple ADV"
    assert sum(opcode == 5 for opcode, operand in chunked(program, 2)) == 1, "program have multiple OUT"
    assert not any(opcode == 3 for opcode, operand in chunked(test_program, 2)), "program include a JNZ inside"

    test_compu = ChronospatialComputer(0, 0, 0, test_program)
    return find(test_compu, program, 0)


def test() -> bool:
    return main(test_input_2) == 117440


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
