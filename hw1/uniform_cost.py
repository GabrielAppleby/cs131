from pancake_stack import PancakeStack
from cake_heap import CakeHeap
from typing import Dict, Tuple, List, Optional


def uniform_cost(initial_state: PancakeStack, goal_state: PancakeStack) -> \
        Optional[Tuple[Dict[PancakeStack, PancakeStack], PancakeStack]]:
    """
    Given an initial state and a goal state finds a series of flips to get
    from the initial state to the goal using the uniform cost algorithm.
    :param initial_state: The initial state to get to the goal from.
    :param goal_state: The goal state to get to from the initial state.
    :return: A tuple containing: a dictionary where each key is a state, and
    each value is that state's parent, and the goal state. None is returned if
    no path is found.
    """
    frontier: CakeHeap = CakeHeap()
    visited: List = []
    path: Dict[PancakeStack, PancakeStack] = {initial_state: None}
    frontier.push(initial_state, 0)

    while not frontier.empty():
        current_state: PancakeStack = frontier.pop()
        visited.append(current_state)
        if goal_state == current_state:
            return path, current_state
        children: List[PancakeStack] = current_state.children()
        for child in children:  # type: PancakeStack
            if child not in visited and child not in frontier:
                frontier.push(child, child.cost_to_self())
                path[child] = current_state
            elif child in frontier and frontier[child].cost_to_self() > \
                    child.cost_to_self():
                frontier.remove(child)
                frontier.push(child, child.cost_to_self())
                path[child] = current_state
    return None
