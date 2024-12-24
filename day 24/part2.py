# https://adventofcode.com/2024/day/24
from __future__ import annotations

from aoc_utils import get_raw_data, process_data, DelayedOP, OPERATIONS


test_input_3 = """
x00: 0
x01: 1
x02: 0
x03: 1
x04: 0
x05: 1
y00: 0
y01: 0
y02: 1
y03: 1
y04: 0
y05: 1

x00 AND y00 -> z05
x01 AND y01 -> z02
x02 AND y02 -> z01
x03 AND y03 -> z03
x04 AND y04 -> z04
x05 AND y05 -> z00
"""


def build_add_gates(size: int) -> list[DelayedOP]:
    # https://www.101computing.net/binary-additions-using-logic-gates/
    gates = [  # half adder
        DelayedOP(OPERATIONS["XOR"], "x00", "y00", "z00"),
        DelayedOP(OPERATIONS["AND"], "x00", "y00", "carry00"),
    ]
    for n in range(1, size):
        x = f"x{n:02}"
        y = f"y{n:02}"
        z = f"z{n:02}"
        cin = f"carry{n-1:02}"
        cout = f"carry{n:02}" if n < size-1 else f"z{n+1:02}"
        # full adder
        gates += [  # first half adder
            DelayedOP(OPERATIONS["XOR"], x, y, f"sum1_{n:02}"),
            DelayedOP(OPERATIONS["AND"], x, y, f"tempcarry1_{n:02}"),
            # second half adder
            DelayedOP(OPERATIONS["XOR"], cin, f"sum1_{n:02}", z),
            DelayedOP(OPERATIONS["AND"], cin, f"sum1_{n:02}", f"tempcarry2_{n:02}"),
            # or gate
            DelayedOP(OPERATIONS["OR"], f"tempcarry1_{n:02}", f"tempcarry2_{n:02}", cout)
        ]
    return gates


def helper_fun(data):
    namespace, gates = process_data(data)

    for i, gate in enumerate(gates):
        op, a, b, c = gate
        a, b = sorted([a, b])
        gates[i] = DelayedOP(op, a, b, c)

    know_gates = [g for g in gates if (g[1][0] in "xy" and g[2][0] in "xy") or g[3][0]=="z"]
    for gate in know_gates:
        print(gate)
    print("----------")
    for gate in gates:
        if gate not in know_gates:
            print(gate)


def main(data):
    print("do it manually, sorry :( ")


def test() -> bool:
    return main(test_input_3) == "z00,z01,z02,z05"


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
