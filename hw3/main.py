import random

from knapsack import Knapsack
from box import Box
from typing import List
from population import Population

# The total population limit
TOTAL_POP_LIMIT: int = 100
# Number of iterations to run the genetic algorithm
NUM_GENERATIONS: int = 10


def reproduce(candidate_one: Knapsack, candidate_two: Knapsack) -> Knapsack:
    """
    Takes two candidates and produces an offspring. In this case adds all of
    the boxes together, then shuffles them up and adds them in that order to
    the new knapsack.
    :param candidate_one: Parent number one.
    :param candidate_two: Parent number two.
    :return: The child.
    """
    new_candidate: Knapsack = Knapsack()
    boxes: List[Box] = candidate_one.contents() + candidate_two.contents()
    random.shuffle(boxes)
    for box in boxes:  # type: Box
        # It is important to remember that the knapsack's put method will not
        # add anything if it is at its capacity, or if that box is already in
        # its bag.
        new_candidate.put(box)
    return new_candidate


def mutate(candidate) -> Knapsack:
    """
    Mutates the given candidate. In this case just calls the knapsack's mutate
    method.
    :param candidate: The candidate to mutate.
    :return: The mutated candidate.
    """
    candidate.mutate(Box.create_boxes())
    return candidate


def cull(population: Population) -> Population:
    """
    Culls the bottom half of the population.
    :param population: The population to cull.
    :return: The top half of the population.
    """
    return population.top_candidates(TOTAL_POP_LIMIT//2)


def genetic_algorithm(population: Population) -> Population:
    """
    Performs the genetic algorithm. To find a fit population.
    :param population: The population to transform.
    :return: The population after transformation.
    """
    # Population created by reproduction and mutation of original population.
    altered_population: Population = Population([])
    for index in range(len(population)):  # type: int
        candidate_one: Knapsack = population.candidate()
        candidate_two: Knapsack = population.candidate()
        child: Knapsack = reproduce(candidate_one, candidate_two)
        if random.randint(1, 100) <= 5:  # type: int
            # Mutate changes the mutable object passed in. Child is just
            # assigned the result for clarity.
            child = mutate(child)
        altered_population.append(child)
    # Population after culling bottom half of population
    culled_population: Population = cull(altered_population)
    # Culled population + a random new population.
    new_population: Population = culled_population.combine(
        Population.new_random_population(TOTAL_POP_LIMIT//2))
    return new_population


def main() -> None:
    """
    Runs everything. Most notably runs the genetic algorithm on the population
    NUM_GENERATIONS times.
    :return: Nothing.
    """
    population: Population = Population.new_random_population(TOTAL_POP_LIMIT)
    print("Starting population:")
    print(population.top_candidates(1))
    for num in range(NUM_GENERATIONS):
        population = genetic_algorithm(population)
    print("Ending population:")
    print(population.top_candidates(1))


if __name__ == '__main__':
    main()
