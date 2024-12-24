# https://adventofcode.com/2024/day/24
from __future__ import annotations

from typing import Iterator, Iterable, NamedTuple, Callable
import itertools_recipes as ir
import operator
from aoc_recipes import mirror_dict

test_input = """
x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02
"""

test_input_2 = """
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
"""

OPERATIONS: dict[str, Callable[[int, int], int]] = {
    "AND": operator.and_,
    "XOR": operator.xor,
    "OR": operator.or_
}
OP_NAMES = mirror_dict(OPERATIONS)


class DelayedOP(NamedTuple):
    op: Callable[[int, int], int]
    var1: str
    var2: str
    result: str

    def __call__(self, namespace: dict[str, int]) -> tuple[str, int]:
        a = namespace[self.var1]
        b = namespace[self.var2]
        namespace[self.result] = self.op(a, b)

    def __str__(self) -> str:
        return f"{self.var1} {OP_NAMES[self.op]} {self.var2} -> {self.result}"


def compute(namespace: dict[str, int], gates: list[DelayedOP]) -> int:
    while gates:
        pending = []
        for gate in gates:
            try:
                gate(namespace)
            except KeyError:
                pending.append(gate)
        if gates == pending:
            raise RuntimeError("all gates are waiting for input")
        gates = pending
    zgates = [g for g in namespace.items() if g[0].startswith("z")]
    zgates.sort(key=lambda x: x[0], reverse=True)
    _, result = zgates.pop(0)
    for _, value in zgates:
        result <<= 1
        result |= value
    return result


def process_data(data: str) -> tuple[dict[str, int], list[DelayedOP]]:
    """transform the raw data into a processable form"""
    variables, operaciones = ir.isplit(data.replace(":", "").splitlines())
    namespace = {k: int(v) for k, v in map(str.split, variables)}
    gates = []
    line: str
    for line in operaciones:
        x, op, y, _, result = line.split()
        gates.append(DelayedOP(OPERATIONS[op], x, y, result))
    return namespace, gates


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
