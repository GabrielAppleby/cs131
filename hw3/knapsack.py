import random

from box import Box
from typing import List


class Knapsack:
    """
    A knapsack capable of carrying any number of boxes as long as their total
    weight is KNAPSACK_CAPACITY or less.
    """

    def __init__(self) -> None:
        """
        Creates an empty knapsack.
        """
        self._boxes: List[Box] = []
        self._weight: int = 0
        self._importance: int = 0
        self._KNAPSACK_CAPACITY: int = 120

    def importance(self) -> int:
        """
        Gets the total importance of all of the things inside of the knapsack.
        :return: The total importance of all of the things inside of the
        knapsack.
        """
        return self._importance

    def contents(self) -> List[Box]:
        """
        The contents of the knapsack. A copy of its list of boxes.
        :return: A copy of this knapsack's list of boxes.
        """
        return self._boxes.copy()

    def put(self, box: Box) -> bool:
        """
        Tries to put a box into the knapsack. Will only succeed if the knapsack
        is not to heavy!
        :param box: The box to attempt to add to the knapsack.
        :return: True if the box is added, false otherwise.
        """
        if (box in self._boxes) or \
                (self._weight + box.weight() > self._KNAPSACK_CAPACITY):
            return False
        else:
            self._weight += box.weight()
            self._importance += box.importance()
            self._boxes.append(box)
            return True

    def fill(self, boxes: List[Box]) -> None:
        """
        Tries to put all of given boxes into the knapsack. Once the knapsack
        is full the rest of the boxes will not be added!
        :param boxes: The boxes to try to add to the knapsack.
        :return: Nothing
        """
        for box in boxes:  # type: box
            self.put(box)

    def mutate(self, boxes: List[Box]) -> None:
        """
        Mutate this knapsack. Take a random box in the knapsack and replace it
        with a random box not already in the knapsack from the boxes
        given.
        :param boxes: The boxes to select the random box to add to the
        knapsack from.
        :return:
        """
        random.shuffle(boxes)
        index: int = random.randint(0, len(self._boxes)-1)
        different_box: Box = self._boxes[index]
        for box in boxes:  # type: box
            if box not in self._boxes:
                different_box = box
                break
        self._boxes[index] = different_box

    def __key(self) -> int:
        """
        Helper function that returns a key to be used in all equality and hash
        related functions.
        :return: The key.
        """
        return self._importance

    def __str__(self) -> str:
        """
        Produces a string output of the Knapsack.
        :return: The string output of the Knapsack.
        """
        return 'Knapsack(Weight: {}. Importance: {})'\
            .format(self._weight, self._importance)

    def __repr__(self) -> str:
        """
        Gets a string representation of the Knapsack.
        :return: A string representation of the Knapsack.
        """
        return 'Knapsack({})'.format(self._boxes)

    def __hash__(self) -> int:
        """
        Gets a hash of the knapsack.
        :return: A hash of the knapsack.
        """
        return hash(self.__key())

    def __eq__(self, other: 'Knapsack') -> bool:
        """
        Determines whether two Knapsacks are equal.
        :param other: The other Knapsack to check for equality.
        :return: A boolean value -- true if they are equal.
        """
        return self.__key() == other.__key()

    def __ne__(self, other: 'Knapsack') -> bool:
        """
        Determines whether two Knapsacks are not equal.
        :param other:  The other Knapsack to check for inequality.
        :return: A boolean value -- true if they are not equal.
        """
        return self.__key() != other.__key()

    def __lt__(self, other: 'Knapsack') -> bool:
        """
        Determines whether this Knapsack is less than the given
        Knapsack.
        :param other: The other Knapsack to compare whether this one is
        less than.
        :return: A boolean value -- true if this Knapsack is less than the
        other one.
        """
        return self.__key() < other.__key()

    def __le__(self, other: 'Knapsack') -> bool:
        """
        Determines whether this Knapsack is less than or equal to the given
        Knapsack.
        :param other: The other Knapsack to compare whether this one is
        less than or equal to.
        :return: A boolean value -- true if this Knapsack is less than or
        equal to the other one.
        """
        return self.__key() <= other.__key()

    def __gt__(self, other: 'Knapsack') -> bool:
        """
        Determines whether this Knapsack is greater than the given
        Knapsack.
        :param other: The other Knapsack to compare whether this one is
        greater than.
        :return: A boolean value -- true if this Knapsack is greater than
        the other one.
        """
        return self.__key() > other.__key()

    def __ge__(self, other: 'Knapsack') -> bool:
        """
        Determines whether this Knapsack is greater than or equal to the
        given Knapsack.
        :param other: The other Knapsack to compare whether this one is
        greater than or equal to.
        :return: A boolean value -- true if this Knapsack is greater than
        or equal to the other one.
        """
        return self.__key() >= other.__key()

