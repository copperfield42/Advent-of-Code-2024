# https://adventofcode.com/2024/day/7
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, calculate2
from math import prod


def main(data: str, verbose: bool = False) -> int:
    """part 1 of the puzzle """
    result = 0
    for j, (n, val) in enumerate(process_data(data), 1):
        minimo = sum(val)
        maximo = prod(v for v in val if v)
        if verbose:
            print(f"{j:03}){n=:_}, {minimo=:_}, {maximo=:_}, {val=}")
        if minimo <= n <= maximo or 1 in val:
            if n in (maximo, minimo) or calculate2(n, val):
                if verbose:
                    print(f"{n=:_} is reachable")
                result += n
            else:
                if verbose:
                    print(f"{n=:_} is not reachable")
        else:
            if verbose:
                print(f"{n=:_} is discarded")
            pass
    return result


def test() -> bool:
    return main(test_input) == 3749


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  # more than 303766878186
