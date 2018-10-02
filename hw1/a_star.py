from pancake_stack import PancakeStack
from cake_heap import CakeHeap
from typing import Dict


def a_star(initial_state: PancakeStack, goal_state: PancakeStack) -> \
        Dict[PancakeStack, PancakeStack]:
    frontier = CakeHeap()
    visited = []
    path = {initial_state: None}
    frontier.push(initial_state, 0)

    while not frontier.empty():
        current_state = frontier.pop()
        visited.append(current_state)
        if goal_state == current_state:
            return path
        children = current_state.children()
        for child in children:
            if child not in visited and child not in frontier:
                frontier.push(child, child.cost_to_goal())
                path[child] = current_state
            elif child in frontier and frontier[child].cost_to_goal() > \
                    child.cost_to_goal():
                frontier.remove(child)
                frontier.push(child, child.cost_to_goal)
                path[child] = current_state
    return {}
