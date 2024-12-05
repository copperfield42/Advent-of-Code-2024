# https://adventofcode.com/2024/day/5
from __future__ import annotations

import itertools_recipes as ir
from ast import literal_eval
from collections import defaultdict


test_input = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


def is_correctly_ordered(printed: tuple[int, ...], rules: dict[int, set[int]]) -> bool:
    for i, pag in enumerate(printed):
        if pag_rule := rules.get(pag):
            for pag_after in pag_rule:
                try:
                    j = printed.index(pag_after)
                    if j < i:
                        return False
                except ValueError:
                    pass
    return True


def process_data(data: str) -> tuple[dict[int, set[int]], list[tuple[int, ...]]]:
    """transform the raw data into a processable form"""
    pages_ordering, updates = ir.isplit(map(str.strip, data.replace("|", ",").strip().splitlines()))
    rules = defaultdict(set)
    for p1, p2 in map(literal_eval, pages_ordering):
        rules[p1].add(p2)
    return rules, list(map(literal_eval, updates))


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
