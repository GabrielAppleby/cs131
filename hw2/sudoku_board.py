from sudoku_tile import SudokuTile
from typing import Set, List


class SudokuBoard:
    """
    Represents a SudokuBoard full of {@link SudokuTiles}.
    """

    # Both the length and width of a Sudoku board.
    BOARD_SIZE: int = 9
    # Both the length and width of a box within the Sudoku board.
    BOX_SIZE: int = 3

    def __init__(self, row_orientation: List[List[int]]):
        """
        Initializes the Sudoku board.
        :param row_orientation: The backing board for this SudokuBoard. Must be
        a standard board as given in PS2.
        """
        self._all_tiles: List[SudokuTile] = []
        self._unassigned_tiles: List[SudokuTile] = []

        # Board in column orientation
        column_orientation: List[List[int]] = \
            SudokuBoard.__column_orientation(row_orientation)

        # Calculate the nine boxes
        list_of_boxes_lists: List[List[int]] = []
        for a in range(0, SudokuBoard.BOARD_SIZE, SudokuBoard.BOX_SIZE):
            for i in range(0, SudokuBoard.BOARD_SIZE, SudokuBoard.BOX_SIZE):
                temp: List[int] = []
                list_of_boxes_lists.append(temp)
                for j in range(0, SudokuBoard.BOX_SIZE):
                    for k in range(0, SudokuBoard.BOX_SIZE):
                        temp.append(row_orientation[j+a][k+i])

        # Turn our lists of rows, columns, and boxes into sets for fast lookup.
        # Although now that I think about it, I've heard that for small lists
        # iterating through might actually be faster than using sets.. Oh well.
        rows: List[Set[int]] = []
        columns: List[Set[int]] = []
        boxes: List[Set[int]] = []
        for i in range(SudokuBoard.BOARD_SIZE):
            rows.append({x for x in row_orientation[i] if x != 0})
            columns.append({x for x in column_orientation[i] if x != 0})
            boxes.append({x for x in list_of_boxes_lists[i] if x != 0})

        # For each tile in give board.
        for i in range(SudokuBoard.BOARD_SIZE):
            for j in range(SudokuBoard.BOARD_SIZE):
                # The tile's value
                value: int = row_orientation[i][j]

                # Calculating which box this tile is in.
                index: int = \
                    ((i // SudokuBoard.BOX_SIZE) * SudokuBoard.BOX_SIZE) + \
                    (j // SudokuBoard.BOX_SIZE)

                # Create a SudokuTile object and give it access to its row,
                # column, box, and value.
                tile: SudokuTile = SudokuTile(
                    rows[i], columns[j], boxes[index], value)

                # Given how we construct our board a value of 0 means that this
                # is one of the tiles we will have to assign a value to.
                if value == 0:
                    self._unassigned_tiles.append(tile)

                # Keep track of all tiles in the board
                self._all_tiles.append(tile)

    def complete(self) -> bool:
        """
        Whether or not the Sudoku board is completely filled in.
        :return: True if the Sudoku board is complete, false otherwise.
        """
        return len(self._unassigned_tiles) == 0

    def unassigned_tiles(self) -> List[SudokuTile]:
        """
        Returns the list of unassigned tiles.
        :return: The list of unassigned tiles.
        """
        return self._unassigned_tiles

    def assign(self, tile: SudokuTile, value: int) -> None:
        """
        Assigns the given value to the tile.
        :param tile: The tile to assign the value.
        :param value: The value to assign the tile.
        :return: Nothing
        """
        tile.assign(value)
        self._unassigned_tiles.remove(tile)

    def unassign(self, tile: SudokuTile) -> None:
        """
        Unassigns the tile given.
        :param tile: The tile to unassign a value.
        :return: Nothing
        """
        tile.unassign()
        self._unassigned_tiles.append(tile)

    def all_tiles(self) -> List[SudokuTile]:
        """
        Returns all of the tiles in the board.
        :return: All of the tiles in the board.
        """
        return self._all_tiles

    def next_tile(self) -> SudokuTile:
        """
        Returns the next tile that should be assigned a value.
        :return: The next tile that should be assigned a value.
        """
        # Since the largest number of possibilities any tile could have is 9
        # we are fine to ust choose an arbitrarily larger starting minimum.
        min_possibilities: int = 99
        min_tile = None
        for current_tile in self.unassigned_tiles():  # type: SudokuTile
            current_possibilities: int = len(current_tile.possible_values())
            if current_possibilities < min_possibilities:
                min_possibilities = current_possibilities
                min_tile = current_tile
        return min_tile

    def __str__(self) -> str:
        """
        Returns the string representation of the board.
        :return: The string representation of the board.
        """
        string_rep = ""
        for index, tile in enumerate(self._all_tiles):
            if index % SudokuBoard.BOARD_SIZE == 0:
                string_rep += '\n'
            string_rep += str(tile) + ','

        return string_rep

    @staticmethod
    def __column_orientation(row_orientation):
        """
        Takes a board in row orientation and returns a board in column
        orientation.
        :param row_orientation: The board to make into a column oriented board.
        :return: The column oriented board.
        """
        column_orientation: List[List[int]] = []
        for i in range(len(row_orientation)):
            column: List[int] = []
            column_orientation.append(column)
            for row in row_orientation:
                column.append(row[i])
        return column_orientation
