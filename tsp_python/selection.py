import random

def tournament_selection(population):
    original_population = population.copy()
    candidates = random.sample(original_population, 2)
    if candidates[0].get_fitness() > candidates[1].get_fitness():
        return candidates[0]
    else:
        return candidates[1]

def biased_random_selection(population):
    # array of fitness values mapping to cities
    fitness_values = [area.get_fitness() for area in population]
    # inverse of fitness value array
    inverse_fitness_values = [sum(fitness_values)/value for value in fitness_values]
    # normalize
    normalized_fitness_values = [value/sum(inverse_fitness_values) for value in inverse_fitness_values]
    # spin the wheel
    random_selection = random.random()
    for i in range(len(population)):
        if random_selection > sum(normalized_fitness_values[:i]):
            return population[i]

def get_parent(population):
    if random.random() > 0.5:
        return tournament_selection(population)
    else:
        return biased_random_selection(population)
