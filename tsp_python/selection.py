import random

from classes import Area


def tournament_selection(population):
    original_population = population.copy()
    candidates = random.sample(original_population, 2)
    #print(f"-- Debug: assessing candidate1={candidates[0]}")
    #print(f"-- Debug: assessing candidate2={candidates[1]}")
    if candidates[0].get_fitness() < candidates[1].get_fitness():
        #print("-- Debug: chose candidate1")
        return candidates[0]
    else:
        #print("-- Debug: chose candidate2")
        return candidates[1]


def biased_random_selection(population, normalized_fitness_values):
    # spin the wheel
    random_selection = random.random()
    #print(f"-- Debug: {normalized_fitness_values}")
    for i in range(len(population)):
        if random_selection < sum(normalized_fitness_values[:i+1]):
            #print(f"--Debug: {random_selection} is less than {sum(normalized_fitness_values[:i])}. Returning")
            return population[i]
    print("ERROR: we shouldn't reach here")


def get_parent(population, normalized_fitness_values):
    if random.random() > 0.5:
        return tournament_selection(population)
    else:
        return biased_random_selection(population, normalized_fitness_values)


def crossover(parentA, parentB):
    #print(f"-- Debug: parentA {' '.join(parentA.get_city_labels())}")
    #print(f"-- Debug: parentB {' '.join(parentB.get_city_labels())}")
    index = random.randrange(1, len(parentA) - 1)
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
