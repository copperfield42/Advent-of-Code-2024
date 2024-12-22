# https://adventofcode.com/2024/day22
from __future__ import annotations
from typing import Iterator, NamedTuple, Iterable
from aoc_utils import get_raw_data, process_data
from aoc_utils import secret_sequence
import itertools_recipes as ir
from tqdm_recipes import progress_bar
from collections import Counter, defaultdict

type SalesSeq = tuple[int, int, int, int]

test_input_2 = """
1
2
3
2024
"""


class SalesWindow(NamedTuple):
    changes_step: SalesSeq
    value: int


def price_sequence(secret: int) -> Iterator[tuple[int, int | None]]:
    """Generator of prices an its change from the given secret value"""
    change = None
    sequence = secret_sequence(secret)
    price = next(sequence) % 10
    yield price, change
    change = price
    for item in sequence:
        price = item % 10
        change = price - change
        yield price, change
        change = price


def changes_windows(secret: int, sample: int = 2000, window: int = 4) -> Iterator[SalesWindow]:
    """Generator of all windows from a price_sequence of the given secret value"""
    for win4 in ir.groupwise(ir.islice(price_sequence(secret), sample), window):
        seq, changes = ir.unzip(win4)
        yield SalesWindow(changes, seq[-1])


def get_sales(sales_seq: SalesSeq, monkey_data: dict[int, dict[SalesSeq, int]]) -> int:
    """sai how many you get from a given sales sequence"""
    return sum(monkey.get(sales_seq, 0) for monkey in monkey_data.values())


def make_sales_history(sales: Iterable[SalesWindow]) -> dict[SalesSeq, int]:
    """make a dict pairing a sales sequence with its value"""
    data = defaultdict(list)
    for changes_step, value in sales:
        data[changes_step].append(value)
    return {k: v[0] for k, v in data.items()}


def main(data: str) -> int:
    """part 2 of the puzzle """
    monkey_data: dict[int, dict[SalesSeq, int]] = {
        i: make_sales_history(changes_windows(secret))
        for i, secret in enumerate(progress_bar(process_data(data), desc="loading"))
    }

    candidatos = Counter(
        sw for sales in progress_bar(monkey_data.values(), desc="candidatos") for sw in sales
    )
    print(f"{len(candidatos)=}")

    cut_off = max(candidatos.values())

    candidatos = [k for k, n in candidatos.items() if n > (cut_off//2)]

    print(f"{len(candidatos)=} after culling")

    return max(get_sales(candidato, monkey_data) for candidato in progress_bar(candidatos, desc="calculating"))



def test() -> bool:
    return main(test_input_2) == 23


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
