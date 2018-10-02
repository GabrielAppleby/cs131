import heapq
from pancake_stack import PancakeStack
from typing import Optional, List, Dict


class CakeHeap:
    """
    CakeHeap defines a wrapper around heapq that allows one to use
    arbitrary objects of type T and specify the costs separately. Currently
    each item and cost is wrapped in a tuple where the 0th element of the tuple
    is the cost and the 1st element is the item. This is an implementation
    detail given to help understand the code and is subject to change!

    If a pancake with the same configuration is removed and then added
    (replaced) with a  higher cost this implementation will not work! Luckily
    I only need to be able to replace pancakes with versions that have lower
    costs. Who would want to pay more for the same pancake anyways?
    """

    def __init__(self) -> None:
        """
        Initialize the underlying heapq.
        """
        self._data: List = []
        self._entries: Dict[PancakeStack, PancakeStack] = {}
        heapq.heapify(self._data)

    def push(self, to_push: PancakeStack, cost: int) -> None:
        """
        Pushes the given item onto the CakeHeap with a cost.
        :param to_push: The item to push onto the CakeHeap.
        :param cost: The cost to associated with the item.
        :return: None.
        """
        self._entries[to_push] = to_push
        heapq.heappush(self._data, (cost, to_push))

    def pop(self) -> Optional[PancakeStack]:
        """
        Pops the item with the lowest cost off of the CakeHeap.
        :return: The item in the CakeHeap with the lowest cost. If empty
        returns None.
        """
        if self.empty():
            return None

        item: PancakeStack = None
        while item is None:
            item = heapq.heappop(self._data)[1]  # type: PancakeStack
            if item in self._entries:
                del self._entries[item]
                return item
            item = None

    def remove(self, to_remove: PancakeStack) -> None:
        """
        Removes the item given from the CakeHeap if it exists.
        :param to_remove: The item to remove.
        :return: None.
        """
        if self.__contains__(to_remove):
            del self._entries[to_remove]

    def empty(self) -> bool:
        """
        Determines whether or not the CakeHeap is empty.
        :return: A boolean value -- true if the CakeHeap is empty.
        """
        return len(self._entries) == 0

    def __contains__(self, to_find: PancakeStack) -> bool:
        """
        Determines if the given item is in the CakeHeap.
        :param to_find: the item to find in the CakeHeap.
        :return: A boolean value -- true if to_find is in the CakeHeap.
        """
        return to_find in self._entries

    def __getitem__(self, to_get: PancakeStack) -> Optional[PancakeStack]:
        """
        Gets an item from the CakeHeap if it exists.
        :param to_get: The item to get from the CakeHeap.
        :return: The item if it is in the CakeHeap, None otherwise.
        """
        return self._entries.get(to_get)

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
