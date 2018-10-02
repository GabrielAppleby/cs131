import heapq
from pancake_stack import PancakeStack
from typing import Optional, List, Tuple


class CakeHeap():
    """
    CakeHeap defines a wrapper around heapq that allows one to use
    arbitrary objects of type T and specify the costs separately. Currently
    each item and cost is wrapped in a tuple where the 0th element of the tuple
    is the cost and the 1st element is the item. This is an implementation
    detail given to help understand the code and is subject to change!
    """

    def __init__(self) -> None:
        """
        Initialize the underlying heapq.
        """
        self._data: List = []
        heapq.heapify(self._data)

    def push(self, to_push: PancakeStack, cost: int) -> None:
        """
        Pushes the given item onto the CakeHeap with a cost.
        :param to_push: The item to push onto the CakeHeap.
        :param cost: The cost to associated with the item.
        :return: None.
        """
        heapq.heappush(self._data, (cost, to_push))

    def pop(self) -> PancakeStack:
        """
        Pops the item with the lowest cost off of the CakeHeap.
        :return: The item in the CakeHeap with the lowest cost.
        """
        return heapq.heappop(self._data)[1]

    def remove(self, to_remove: PancakeStack) -> None:
        """
        Removes the item given from the CakeHeap.
        :param to_remove: The item to remove.
        :return: None.
        """
        for item in self._data:  # type: Tuple[int, PancakeStack]
            if item[1] == to_remove:
                self._data[item[0]] = self._data[-1]
                self._data.pop()
                heapq.heapify(self._data)

    def empty(self) -> bool:
        """
        Determines whether or not the CakeHeap is empty.
        :return: A boolean value -- true if the CakeHeap is empty.
        """
        return len(self._data) == 0

    def __contains__(self, to_find: PancakeStack) -> bool:
        """
        Determines if the given item is in the CakeHeap.
        :param to_find: the item to find in the CakeHeap.
        :return: A boolean value -- true if to_find is in the CakeHeap.
        """
        for item in self._data:  # type: Tuple[int, PancakeStack]
            if item[1] == to_find:
                return True
        return False

    def __getitem__(self, to_get: PancakeStack) -> Optional[PancakeStack]:
        """
        Gets an item from the CakeHeap if it exists.
        :param to_get: The item to get from the CakeHeap.
        :return: The item if it is in the CakeHeap, None otherwise.
        """
        for item in self._data: # type: Tuple[int, PancakeStack]
            if item[1] == to_get:
                return item[1]
        return None

    def __str__(self) -> str:
        """
        Produces a string output of the CakeHeap.
        :return: The string output of the CakeHeap.
        """
        return 'CakeHeap({})'.format(self._data)

    def __repr__(self) -> str:
        """
        Produces a string representation of the PancakeHeap object.
        :return: The string representation of the PancakeHeap object.
        """
        return 'CakeHeap({})'.format(self._data)
