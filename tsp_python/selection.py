import random

from classes import Area


def tournament_selection(population):
    original_population = population.copy()
    candidates = random.sample(original_population, 2)
    if candidates[0].get_fitness() > candidates[1].get_fitness():
        return candidates[0]
    else:
        return candidates[1]


def biased_random_selection(population, normalized_fitness_values):
    # spin the wheel
    random_selection = random.random()
    for i in range(len(population)):
        if random_selection > sum(normalized_fitness_values[:i]):
            return population[i]


def get_parent(population, normalized_fitness_values):
    for area in population:
        assert len(area.cities) == 10
    if random.random() > 0.5:
        return tournament_selection(population)
    else:
        return biased_random_selection(population, normalized_fitness_values)


def crossover(parentA, parentB):
    #print(f"-- Debug: parentA {' '.join(parentA.get_city_labels())}")
    #print(f"-- Debug: parentB {' '.join(parentB.get_city_labels())}")
    index = random.randrange(len(parentA))
    #print(f"-- Debug: index={index}")
    new_offspring = parentA.cities[:index]
    new_offspring_ids = [c.id for c in new_offspring]
    #print(f"-- Debug: new_offspring={[c.id for c in new_offspring]}")
    second = [e for e in parentB.cities if e.id not in new_offspring_ids]
    #print(f"-- Debug: second={[c.id for c in second]}")
    new_offspring.extend(second)
    #print(f"-- Debug: len(new_offspring)={len(new_offspring)}")
    return Area(new_offspring)


def get_offspring(parentA, parentB):
    offspringA = crossover(parentA, parentB)
    offspringB = crossover(parentB, parentA)
    return offspringA, offspringB
