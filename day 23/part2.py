# https://adventofcode.com/2024/day/23
from __future__ import annotations
from typing import Callable, Iterable, Iterator
from aoc_utils import test_input, get_raw_data, process_data
from functools import partial


def BronKerbosch1[V](R: frozenset[V], P: frozenset[V], X: frozenset[V], N: Callable[[V], frozenset[V]]) -> Iterator[frozenset[V]]:
    if not P and not X:
        yield R
    for v in P:
        sv = frozenset([v])
        yield from BronKerbosch1(R | sv, P & N(v), X & N(v), N=N)
        P = P - sv
        X = X | sv
    pass


def maximum_clique[Graph, V](graph: Graph, neighbor: Callable[[Graph, V], frozenset[V]], vertices: Callable[[Graph], Iterable[V]] = iter) -> Iterator[frozenset[V]]:
    """Bron–Kerbosch algorithm
    https://stackoverflow.com/questions/2801138/find-all-complete-sub-graphs-within-a-graph
    https://en.wikipedia.org/wiki/Clique_problem
    https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm

    find the maximum cliques in a graph, that is a sub graph such that every 2 vertex are connected with one another

    """
    return BronKerbosch1(R=frozenset(), P=frozenset(vertices(graph)), X=frozenset(), N=partial(neighbor, graph))


def main(data: str) -> str:
    """part 2 of the puzzle """
    connections = process_data(data)
    cliques = set(maximum_clique(connections, dict.get))
    assert cliques, "no cliques found"
    size = max(map(len, cliques))
    max_clique = [cli for cli in cliques if len(cli) == size]
    assert len(max_clique) == 1, f"many maximum cliques"
    return ",".join(sorted(max_clique[0]))


def test() -> bool:
    return main(test_input) == "co,de,ka,ta"


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
