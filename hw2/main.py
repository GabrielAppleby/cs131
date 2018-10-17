from sudoku_board import SudokuBoard
from sudoku_tile import SudokuTile
from typing import Set, Optional

# The initial form of the board.
INITIAL_BOARD = [
    [6, 0, 8, 7, 0, 2, 1, 0, 0],
    [4, 0, 0, 0, 1, 0, 0, 0, 2],
    [0, 2, 5, 4, 0, 0, 0, 0, 0],
    [7, 0, 1, 0, 8, 0, 4, 0, 5],
    [0, 8, 0, 0, 0, 0, 0, 7, 0],
    [5, 0, 9, 0, 6, 0, 3, 0, 1],
    [0, 0, 0, 0, 0, 6, 7, 5, 0],
    [2, 0, 0, 0, 9, 0, 0, 0, 8],
    [0, 0, 6, 8, 0, 5, 2, 0, 3]]

# Arto Inkala's board
ARTO_BOARD = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]]

# Broken board
UNSOLVABLE_BOARD = [
    [6, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 6, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]]


def greet_user(board: SudokuBoard) -> None:
    """
    Greets the user.
    :return: None.
    """
    print("\nWelcome! I am the Sudoku-Solver-9000.\n\n"
          "My initial board to solve is:")
    print(board)
    print("\nBlue indicates that the value was given to me. Red indicates\n"
          "that I will solve (if it is 0) or have solved (if it is not 0) \n"
          "for this value. It is possible that colors will not work in your\n"
          "terminal, if so just refer to the numbers that change from 0 to\n"
          "some number between 1-9.\n")

def display_answer(board: SudokuBoard) -> None:
    """
    Displays the answer
    :return: None.
    """
    if board is not None:
        print("The solved board is:")
        print(board)
    else:
        print("The given board was not solvable. Or I'm getting demoted to "
              "the Sudoku-Solver-8000.")


def recursive_backtracking(board: SudokuBoard) -> Optional[SudokuBoard]:
    """
    Recursive backtracking algorithm for solving Sudoku. It uses a form of
    Forward Checking and Minimum Remaining Values to speed up the process.
    :param board: The SudokuBoard to solve.
    :return: The solved SudokuBoard is possible, None otherwise.
    """
    # If the board is complete, return it.
    if board.complete() is True:
        return board
    # Otherwise grab the next tile. This step uses the Minimum Remaining Values
    # technique to find the next tile to assign.
    tile: SudokuTile = board.next_tile()
    if tile is not None:
        # This grabs the possible values available for the current tile
        # A form of forward checking -- eliminating possibilities that will
        # will break the constraints right away.
        possible_values: Set[int] = tile.possible_values()
        for value in possible_values:  # type: int
            # Attempt to assign a value
            board.assign(tile, value)
            # Attempt to go through the process for the rest of the tiles
            result = recursive_backtracking(board)
            # If it worked
            if result is not None:
                # Return the result!
                return result
            # Otherwise, unassign the tile
            board.unassign(tile)
            # Now we either try the next value for this tile or if there
            # are no more possible value for this tile we return None and try
            # reassigning the variable before this.
        return None
    return None


if __name__ == "__main__":
    my_board: SudokuBoard = SudokuBoard(INITIAL_BOARD)
    greet_user(my_board)
    answer: SudokuBoard = recursive_backtracking(my_board)
    display_answer(answer)


