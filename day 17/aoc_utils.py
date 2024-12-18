# https://adventofcode.com/2024/day/17
from __future__ import annotations

from typing import Iterator, Iterable, Literal
import itertools_recipes as ir
import dataclasses
import re


test_input = """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""

@dataclasses.dataclass
class ChronospatialComputer:
    register_a: int
    register_b: int
    register_c: int
    program: tuple[Literal[0, 1, 2, 3, 4, 5, 6, 7], ...]
    instruction: int = 0
    output: list[int] = dataclasses.field(default_factory=list)

    def setup(self, a: int = 0, b: int = 0, c: int = 0) -> None:
        self.register_a = a
        self.register_b = b
        self.register_c = c

    def combo_operand(self, value: int) -> int:
        match value:
            case 4:
                return self.register_a
            case 5:
                return self.register_b
            case 6:
                return self.register_c
            case 7:
                raise ValueError("reserve combo operand")
            case themselves:
                return themselves

    def adv(self, operand: int) -> None:
        self.register_a = self.register_a >> self.combo_operand(operand)
        self.instruction += 2

    def bxl(self, operand: int) -> None:
        self.register_b = self.register_b ^ operand
        self.instruction += 2

    def bst(self, operand: int) -> None:
        self.register_b = self.combo_operand(operand) % 8
        self.instruction += 2

    def jnz(self, operand: int):
        if not self.register_a:
            self.instruction += 2
            return
        self.instruction = operand

    def bxc(self, operand: int) -> None:
        self.register_b = self.register_b ^ self.register_c
        self.instruction += 2

    def out(self, operand: int) -> None:
        self.output.append(self.combo_operand(operand) % 8)
        self.instruction += 2

    def bdv(self, operand: int) -> None:
        self.register_b = self.register_a // (2**self.combo_operand(operand))
        self.instruction += 2

    def cdv(self, operand: int) -> None:
        self.register_c = self.register_a // (2 ** self.combo_operand(operand))
        self.instruction += 2

    def run(self) -> tuple[int, ...]:
        self.output.clear()
        self.instruction = 0
        opcode = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }
        try:
            while True:
                function = opcode[self.program[self.instruction]]
                function(self.program[self.instruction+1])
        except IndexError:
            pass
        return tuple(self.output)


def process_data(data: str) -> ChronospatialComputer:
    """transform the raw data into a processable form"""
    a, b, c, *p = map(int, re.findall(r"[0-9]+", data))
    assert all(i in range(8) for i in p), "invalid program"
    return ChronospatialComputer(a, b, c, tuple(p))

    pass


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
