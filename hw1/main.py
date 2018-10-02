from pancake_stack import PancakeStack
from a_star import a_star
from uniform_cost import uniform_cost
from typing import Tuple, Optional, Dict, List

START_COST_TO_PARENT = 0


def print_path(
        path_and_goal: Tuple[Dict[PancakeStack, PancakeStack], PancakeStack]) \
        -> None:
    """
    Print the solution path.
    :param path_and_goal: A tuple containing: a dictionary where each key is a
    state, and each value is that state's parent, and the goal state. Can be
    None if no path exists.
    :return: None
    """
    if path_and_goal is None:
        print("No solution")
        return
    current: PancakeStack = path_and_goal[1]
    path: Dict[PancakeStack, PancakeStack] = path_and_goal[0]
    while True:
        print(current)
        if path.get(current) is None:
            return
        current = path[current]


def convert_to_cake(user_input: str) -> Optional[PancakeStack]:
    """
    Converts user input into a PancakeStack if possible.
    :param user_input: The string to attempt to convert to a PancakeStack.
    :return: The PancakeStack if successful, None otherwise.
    """
    integers: List[int] = [int(x) for x in user_input.split(',')]
    sorted_integers: List[int] = sorted(integers)
    for index, item in enumerate(sorted_integers):  # type: int, int
        if item != (index+1):
            return None
    return PancakeStack(integers, START_COST_TO_PARENT)


def greet_user() -> None:
    """
    Greets the user.
    :return: None.
    """
    print("Welcome! I am the Pancake-Stack-Solver-9000.")
    print("Please enter the ordering of your initial stack and I will find "
          "the number of flips needed to return it to the proper ordering.")
    print("The first number entered will be treated as the bottom of the "
          "stack. The last number entered as the top of the stack.")
    print("The larger the number the larger the pancake. 5 is a much larger "
          "pancake than 1.")
    print("The integers must start at 1 and cannot skip.")
    print("For example: 5, 4, 3, 2, 1 -- would be treated as a stack in the "
          "correct order from the bottom to the top")


def get_input() -> str:
    """
    Gets input from the user.
    :return: None
    """
    return input("Please input your initial stack as a comma separated list "
                 "of integers that follow the rules above. Anything else "
                 "will be rejected.\n")


if __name__ == "__main__":
    initial_cake: PancakeStack = None

    greet_user()

    while initial_cake is None:
        try:
            initial_cake = convert_to_cake(get_input())
        except ValueError:
            pass

    goal_cake: PancakeStack = PancakeStack(
        sorted(initial_cake.get_data(), reverse=True), -1)

    star_result = a_star(initial_cake, goal_cake)
    uniform_result = uniform_cost(initial_cake, goal_cake)

    print("A* result:")
    print_path(star_result)
    print("Uniform-cost result:")
    print_path(uniform_result)
