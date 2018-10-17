from typing import Set, List


class SudokuTile:
    """
    Represents an individual tile that can hold a value in a Sudoku board.
    """

    # The universe of possible values a Sudoku tile could take on.
    UNIVERSE_OF_TILE_VALUES: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Colors
    C_BLUE = '\u001b[34m'
    C_RED = '\u001b[31m'
    C_END = '\033[0m'

    def __init__(self,
                 row: Set[int],
                 column: Set[int],
                 box: Set[int],
                 value: int):
        """
        Initializes the SudokuTile by assigning a value (0 if none), and giving
        the tile access to its row, column, and surrounding box.
        :param row: The row this tile resides in.
        :param column: The column this tile resides in.
        :param box: The box this tile resides in.
        :param value: The value of this tile (0 if none).
        """
        self._row: Set[int] = row
        self._column: Set[int] = column
        self._box: Set[int] = box
        self._value: int = value
        self._color: str = SudokuTile.C_BLUE if value != 0 else SudokuTile.C_RED

    def possible_values(self) -> Set[int]:
        """
        Gets all of the possible values this tile could take on.
        :return: The set of possible values this tile could take on. Can be
        empty.
        """
        return {x for x in SudokuTile.UNIVERSE_OF_TILE_VALUES if
                (x not in self._row) and
                (x not in self._column) and
                (x not in self._box)}

    def assign(self, value: int) -> None:
        """
        Assign a value to this tile.
        :param value: The value to assign.
        :return: Nothing.
        """
        self._value = value
        self._row.add(value)
        self._column.add(value)
        self._box.add(value)

    def unassign(self) -> None:
        """
        Unassigns the current value of this tile.
        :return: Nothing.
        """
        self._row.remove(self._value)
        self._column.remove(self._value)
        self._box.remove(self._value)
        self._value = 0

    def __str__(self) -> str:
        """
        Returns the string representation of the tile.
        :return: The string representation of the tile.
        """
        return self._color + str(self._value) + SudokuTile.C_END
