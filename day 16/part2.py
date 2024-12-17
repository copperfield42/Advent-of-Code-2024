# https://adventofcode.com/2024/day/16
from __future__ import annotations
from typing import Iterator
from aoc_utils import test_input_1, test_input_2, get_raw_data, process_data
from aoc_utils import find_best_path, Node, Matrix, Point, a_star_shortest_path, DIRECCIONES
from aoc_utils import neighbors, edge_cost, make_is_target, make_heuristic, where2
from tqdm_recipes import progress_bar
from aoc_recipes.priority_queue import PriorityQueue
from aoc_recipes import DefaultValueDict, set_recursion_limit
from collections import defaultdict


def find_all_best_paths[Path: tuple[Node, ...]](mapa: Matrix[str], start: Node, goal: Point) -> Iterator[Path]:
    # https://www.youtube.com/watch?v=BJhpteqlVPM
    is_target = make_is_target(goal)
    heuristic = make_heuristic(goal)
    best_cost, best_path = a_star_shortest_path(mapa, start, is_target, neighbors, edge_cost, heuristic=heuristic)

    if not best_path:
        return

    def is_target_path(current_path: Path) -> bool:
        return is_target(current_path[-1])

    def build_path(old_path: Path, next_step) -> Path:
        return old_path + (next_step,)

    visitados: set[Node] = set()

    queue: PriorityQueue[tuple[int, Node]] = PriorityQueue()  # (cost, Node)
    queue.add_task((0, start), 0)

    lowest_cost: DefaultValueDict[Node, int | float] = DefaultValueDict(float("inf"))
    lowest_cost[start] = 0

    backtrack: dict[Node, set[Node]] = defaultdict(set)
    end_state: set[Node] = set()

    while queue:
        cost, position = queue.pop_task()

        if cost > lowest_cost[position]:
            continue

        if is_target(position):
            if cost > best_cost:
                break
            end_state.add(position)

        for next_position in neighbors(mapa, position):
            next_cost = edge_cost(mapa, position, next_position, cost)
            curent_lowest = lowest_cost[next_position]
            if next_cost > curent_lowest:
                continue
            if next_cost < curent_lowest:
                backtrack[next_position].clear()
                lowest_cost[next_position] = next_cost
            backtrack[next_position].add(position)
            queue.add_task((next_cost, next_position), next_cost + heuristic(next_position))

    with set_recursion_limit(len(best_path)*2):
        for end in end_state:
            yield from rebuild_paths(start, end, backtrack, (end,))


def rebuild_paths(start: Node, end: Node, traces: dict[Node, set[Node]], path: tuple[Node, ...]=None) -> Iterator[tuple[Node, ...]]:
    if path is None:
        path = (end,)
    if start == end:
        yield path
        return

    for item in traces.get(end, []):
        yield from rebuild_paths(start, item, traces, path+(item,))





def main(data: str) -> int:
    """part 2 of the puzzle """
    start, target, mapa = process_data(data)
    print(f"\n\nfinding best path from {start=} to {target=}...")
    cost, path = find_best_path(mapa, start, target)
    print(f"best path: {cost=} {len(path)=}")
    print("finding all best paths...")
    paths = list(find_all_best_paths(mapa, start, target))
    print(f"find {len(paths)} path with sizes of {set(len(p) for p in paths)}")
    assert tuple(path[::-1]) in paths
    return len({n.position for p in paths for n in p})


def test() -> bool:
    assert main(test_input_1) == 45, "fail example 1"
    assert main(test_input_2) == 64, "fail example 2"
    return True


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    part2_data = get_raw_data()
    print("solution part2:", main(part2_data))  #
