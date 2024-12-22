# https://adventofcode.com/2024/day/21
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import NUMERIC_KEYPAD, DIRECTIONAL_KEYPAD, make_path
from tqdm_recipes import progress_bar


def main(data: str) -> int:
    """part 1 of the puzzle """
    # https://www.youtube.com/watch?v=dqzAaj589cM
    result = 0
    codes = process_data(data)
    for i, code in enumerate(codes, 1):
        print(code, f"{i}/{len(codes)}")
        rutas = list(make_path(NUMERIC_KEYPAD, code))
        for _ in range(2):
            next_rutas = [new for old in progress_bar(rutas) for new in make_path(DIRECTIONAL_KEYPAD, old)]
            best_len = min(map(len, next_rutas))
            rutas = [x for x in next_rutas if len(x) == best_len]
            print("filter", len(next_rutas)-len(rutas), "of", len(next_rutas),"total")
        print()
        print(f"{best_len=}")
        print("-"*12)
        result += best_len*int(code[:-1])

    return result


def test() -> bool:
    return main(test_input) == 126384


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    part1_data = get_raw_data()
    print("solution part1:", main(part1_data))  #
