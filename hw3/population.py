import random

from box import Box
from knapsack import Knapsack
from typing import List, Optional


class Population:
    """
    A population of knapsacks.
    """

    @staticmethod
    def new_random_population(number_of_individuals: int) -> 'Population':
        """
        Creates a new random population of knapsacks.
        :param number_of_individuals: The number of knapsacks to have in the
        population.
        :return: The new random population.
        """
        boxes: List[Box] = Box.create_boxes()
        knapsacks: List[Knapsack] = []
        for index in range(number_of_individuals):  # type: int
            random.shuffle(boxes)
            knapsack: Knapsack = Knapsack()
            knapsack.fill(boxes)
            knapsacks.append(knapsack)
        return Population(knapsacks)

    def __init__(self, knapsacks: List[Knapsack]):
        """
        Creates a new population given some knapsacks.
        :param knapsacks: The knapsacks to start the population with.
        """
        self._knapsacks: List[Knapsack] = knapsacks
        total_importance: int = 0
        for knapsack in knapsacks:  # type: Knapsack
            total_importance += knapsack.importance()
        self._total_importance: int = total_importance

    def candidate(self) -> Optional[Knapsack]:
        """
        Picks a candidate from the population. Each knapsack is selected with
        probability proportional to its importance / fitness.
        :return: The candidate selected.
        """
        target_index: int = random.randint(1, self._total_importance)
        importance_accumulator: int = 0
        for knapsack in self._knapsacks:  # type: Knapsack
            importance_accumulator += knapsack.importance()
            if importance_accumulator >= target_index:
                return knapsack
        return None

    def top_candidates(self, num: int) -> 'Population':
        """
        The num candidates with the greatest importance.
        :param num: The number of candidates to return.
        :return: A population with the num candidates with the greatest
        importance.
        """
        # Sorts least to greatest
        self._knapsacks.sort()
        # So grab the last num elements.
        return Population(self._knapsacks[-num:])

    def append(self, knapsack: Knapsack) -> None:
        """
        Add another knapsack to this population.
        :param knapsack: The knapsack to add.
        :return: Nothing.
        """
        self._knapsacks.append(knapsack)
        self._total_importance += knapsack.importance()

    def combine(self, other_population: 'Population') -> 'Population':
        """
        Combine this population with another and return the result.
        :param other_population: The other population to combine with.
        :return: The new population / combination.
        """
        combined_knapsacks = self._knapsacks + other_population._knapsacks
        return Population(combined_knapsacks)

    def contents(self) -> List[Knapsack]:
        """
        Gets all of the knapsacks in this population.
        :return: All of the knapsacks in this population.
        """
        return self._knapsacks.copy()

    def total_importance(self) -> int:
        """
        Gets the total importance of this population. This is the importance
        of each knapsack added up.
        :return: The total importance of this population.
        """
        return self._total_importance

    def __len__(self) -> int:
        """
        Gets the length of the population. The number of different knapsacks
        it holds.
        :return: The length of the population.
        """
        return len(self._knapsacks)

    def __str__(self) -> str:
        """
        Produces a string output of the Knapsack.
        :return: The string output of the Knapsack.
        """
        return 'Population(Knapsacks: {}. Importance: {})'\
            .format(self._knapsacks, self._total_importance)

    def __repr__(self) -> str:
        """
        Gets a string representation of the Knapsack.
        :return: A string representation of the Knapsack.
        """
        return 'Population({})'.format(self._knapsacks)
