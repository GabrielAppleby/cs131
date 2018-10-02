from typing import Sequence, List


class PancakeStack:
    """
    A representation of a stack of pancakes where the 0th index of the internal
    representation (_data) is the bottom of the stack, and the (len(_data)-1)th
    index is the top of the stack.
    """

    def __init__(self, data: Sequence[int], cost_to_parent: int):
        """
        Initializes the stack of pancakes.
        :param data: The list representation of the pancake stack. The 0th
        index must be the bottom of the stack, and the (len(_data)-1)th index
        must be the top of the stack.
        :param cost_to_parent: The cost associated with the parent.
        """
        self._data = tuple(data)
        self._length = len(data)
        self._cost_to_parent = cost_to_parent
        self._heuristic_cost = self.__calculate_heuristic_cost()

    def cost_to_parent(self) -> int:
        """
        Gets the cost to the "parent" state, or the state that preceded this
        one.
        :return: The cost to get the "parent" state.
        """
        return self._cost_to_parent

    def cost_to_goal(self) -> int:
        """
        Gets the cost to the goal from the start. Note: uses a heuristic to get
        from the current node to the goal.
        :return: The cost to the goal from the start.
        """
        return self.cost_to_parent() + self.__actual_cost_between_states() + \
            self._heuristic_cost

    def cost_to_self(self) -> int:
        """
        Gets the cost to this state from the start state.
        :return: The cost to get to this state from the start state.
        """
        return self.cost_to_parent() + self.__actual_cost_between_states()

    def children(self) -> List['PancakeStack']:
        """
        Gets the "children" of the current state, (all states it is possible to
        get to in one flip.
        :return: The children of the current state.
        """
        children = []
        for i in range(self.__len__()):
            children.append(PancakeStack(self._data[0:i] +
                                         tuple(reversed(
                                             self._data[i:self.__len__()])),
                                         self._cost_to_parent +
                                         self.__actual_cost_between_states()))
        return children

    def __actual_cost_between_states(self) -> int:
        """
        Gets the actual cost to move from one state to another.
        :return: The actual cost to move from one state to another.
        """
        return 20 + self.__len__()

    def __calculate_heuristic_cost(self) -> int:
        """
        Calculates and returns the heuristic cost for this state. (The
        estimated cost to get to the goal from this state.)
        :return: The estimated cost.
        """
        cost = 0
        for pancake, index in enumerate(self._data):
            if pancake != (index + 1):
                cost += 1
        return cost

    def __key(self) -> Sequence[int]:
        """
        Helper function that returns a key to be used in all equality and hash
        related functions.
        :return: The key.
        """
        return self._data

    def __len__(self) -> int:
        """
        Gets the length of this PancakeStack. (The number of pancakes in the
        stack.
        :return: The length of the PancakeStack.
        """
        return self._length

    def __getitem__(self, index: int) -> int:
        """
        Gets the item at the given index of the PancakeStack.
        :param index:
        :return: The item at that index.
        """
        return self._data[index]

    def __hash__(self) -> int:
        """
        Gets a hash of the PancakeStack.
        :return: A hash of the PancakeStack. (There is a breakfast joke in
        there somewhere...)
        """
        return hash(self.__key())

    def __repr__(self) -> str:
        """
        Gets a string representation of the PancakeStack.
        :return: A string representation of the PancakeStack.
        """
        return 'PancakeStack({})'.format(self._data)

    def __eq__(self, other: 'PancakeStack') -> bool:
        """
        Determines whether two pancakes stacks are equal.
        :param other: The other PancakeStack to check for equality.
        :return: A boolean value -- true if they are equal.
        """
        return self.__key() == other.__key()

    def __ne__(self, other: 'PancakeStack') -> bool:
        """
        Determines whether two pancakes stacks are not equal.
        :param other:  The other PancakeStack to check for inequality.
        :return: A boolean value -- true if they are not equal.
        """
        return self.__key() != other.__key()

    def __lt__(self, other: 'PancakeStack') -> bool:
        """
        Determines whether this PancakeStack is less than the given
        PancakeStack.
        :param other: The other PancakeStack to compare whether this one is
        less than.
        :return: A boolean value -- true if this PancakeStack is less than the
        other one.
        """
        return self.__key() < other.__key()

    def __le__(self, other: 'PancakeStack') -> bool:
        """
        Determines whether this PancakeStack is less than or equal to the given
        PancakeStack.
        :param other: The other PancakeStack to compare whether this one is
        less than or equal to.
        :return: A boolean value -- true if this PancakeStack is less than or
        equal to the other one.
        """
        return self.__key() <= other.__key()

    def __gt__(self, other: 'PancakeStack') -> bool:
        """
        Determines whether this PancakeStack is greater than the given
        PancakeStack.
        :param other: The other PancakeStack to compare whether this one is
        greater than.
        :return: A boolean value -- true if this PancakeStack is greater than
        the other one.
        """
        return self.__key() > other.__key()

    def __ge__(self, other: 'PancakeStack') -> bool:
        """
        Determines whether this PancakeStack is greater than or equal to the
        given PancakeStack.
        :param other: The other PancakeStack to compare whether this one is
        greater than or equal to.
        :return: A boolean value -- true if this PancakeStack is greater than
        or equal to the other one.
        """
        return self.__key() >= other.__key()
