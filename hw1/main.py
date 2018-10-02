from pancake_stack import PancakeStack
from a_star import a_star

GOAL_STATE = PancakeStack([5, 4, 3, 2, 1], 0)


def print_path(path):
    if len(path) == 0:
        print("No solution")
        return
    current = GOAL_STATE
    while True:
        print(current)
        if path.get(current) is None:
            return
        current = path[current]


if __name__ == "__main__":
    stack_of_pancakes = PancakeStack([4, 5, 1, 3, 2], 0)
    print_path(a_star(stack_of_pancakes, GOAL_STATE))
