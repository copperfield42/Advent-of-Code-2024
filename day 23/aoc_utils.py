# https://adventofcode.com/2024/day/23
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir
from collections import defaultdict


test_input = """
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
"""


def process_data(data: str) -> dict[str, frozenset[str]]:
    """transform the raw data into a processable form"""
    connections = defaultdict(set)
    for line in ir.interesting_lines(data):
        a, b = line.split("-")
        connections[a].add(b)
        connections[b].add(a)
    return {k: frozenset(v) for k, v in connections.items()}


def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()
