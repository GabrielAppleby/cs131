from typing import List, Tuple


class Box:
    """
    A box holding something that has importance and weight.
    """

    @staticmethod
    def create_boxes() -> List['Box']:
        """
        Creates and returns the boxes listed in the assignment.
        :return: The list of boxes from the assignment.
        """
        boxes: List['Box'] = [
            Box(20, 6),
            Box(30, 5),
            Box(60, 8),
            Box(90, 7),
            Box(50, 6),
            Box(70, 9),
            Box(30, 4)]
        return boxes

    def __init__(self, weight: int, importance: int):
        """
        Creates a box given its weight and importance.
        :param weight: How heavy the box is.
        :param importance: How important the box is.
        """
        self._weight: int = weight
        self._importance: int = importance

    def importance(self) -> int:
        """
        Gets the importance of this box.
        :return: The importance of this box.
        """
        return self._importance

    def weight(self) -> int:
        """
        Gets the weight of this box.
        :return: The weight of this box.
        """
        return self._weight

    def __key(self) -> Tuple[int, int]:
        """
        Helper function that returns a key to be used in all equality and hash
        related functions.
        :return: The key.
        """
        return self.importance(), self.weight()

    def __str__(self) -> str:
        """
        Produces a string output of the Box.
        :return: The string output of the Box.
        """
        return 'Box(Weight: {}. Importance: {})'\
            .format(self.weight(), self.importance())

    def __repr__(self) -> str:
        """
        Gets a string representation of the Box.
        :return: A string representation of the Box.
        """
        return 'Box({}, {})'.format(self.weight(), self.importance())

    def __hash__(self) -> int:
        """
        Gets a hash of the Box.
        :return: A hash of the Box.
        """
        return hash(self.__key())

    def __eq__(self, other: 'Box') -> bool:
        """
        Determines whether two Boxes are equal.
        :param other: The other Box to check for equality.
        :return: A boolean value -- true if they are equal.
        """
        return self.__key() == other.__key()

    def __ne__(self, other: 'Box') -> bool:
        """
        Determines whether two Boxes are not equal.
        :param other:  The other Box to check for inequality.
        :return: A boolean value -- true if they are not equal.
        """
        return self.__key() != other.__key()

    def __lt__(self, other: 'Box') -> bool:
        """
        Determines whether this Box is less than the given
        Box.
        :param other: The other Box to compare whether this one is
        less than.
        :return: A boolean value -- true if this Box is less than the
        other one.
        """
        return self.__key() < other.__key()

    def __le__(self, other: 'Box') -> bool:
        """
        Determines whether this Box is less than or equal to the given
        Box.
        :param other: The other Box to compare whether this one is
        less than or equal to.
        :return: A boolean value -- true if this Box is less than or
        equal to the other one.
        """
        return self.__key() <= other.__key()

    def __gt__(self, other: 'Box') -> bool:
        """
        Determines whether this Box is greater than the given
        Box.
        :param other: The other Box to compare whether this one is
        greater than.
        :return: A boolean value -- true if this Box is greater than
        the other one.
        """
        return self.__key() > other.__key()

    def __ge__(self, other: 'Box') -> bool:
        """
        Determines whether this Box is greater than or equal to the
        given Box.
        :param other: The other Box to compare whether this one is
        greater than or equal to.
        :return: A boolean value -- true if this Box is greater than
        or equal to the other one.
        """
        return self.__key() >= other.__key()