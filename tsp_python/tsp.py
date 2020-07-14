import math
import random

from selection import get_parent, get_offspring
from classes import Area, City


def argmax(population):
    score = math.inf
    best = None
    for area in population:
        current = area.get_fitness()
        if current < score:
            best = area
            score = current
    return best


def initialize_areas(num_areas, num_cities_per_area, x_y_grid_size=10):
    """Returns array of Area objects"""
    areas = list()
    cities = list()

    for i, _ in enumerate(range(num_cities_per_area)):
        x = random.uniform(0, x_y_grid_size)
        y = random.uniform(0, x_y_grid_size)
        cities.append(City(x, y, i))

    for _ in range(num_areas):
        random.shuffle(cities)
        areas.append(Area(cities.copy()))
    return areas


def spawn_population(num_areas):
    return initialize_areas(num_areas, 20)


def get_best_area(population):
    return argmax(population)


def evolve(population):
    offspring = list()
    # array of fitness values mapping to cities
    fitness_values = [area.get_fitness() for area in population]
    # inverse of fitness value array
    inverse_fitness_values = [sum(fitness_values) / value for value in fitness_values]
    # normalize
    normalized_fitness_values = [
        value / sum(inverse_fitness_values) for value in inverse_fitness_values
    ]
    while len(offspring) < len(population):
        # Get parents
        p1 = get_parent(population, normalized_fitness_values)
        p2 = get_parent(population, normalized_fitness_values)
        # print(f"-- Debug: parent1= {' '.join(p1.get_city_labels())}")
        while p1.get_city_labels() == p2.get_city_labels():
            p2 = get_parent(population, normalized_fitness_values)
        # print(f"-- Debug: parent2= {' '.join(p2.get_city_labels())}")

        # Crossover
        offspringA, offspringB = get_offspring(p1, p2)
        # print(f"-- Debug: offspringA= {' '.join(offspringA.get_city_labels())}")
        # print(f"-- Debug: offspringB= {' '.join(offspringB.get_city_labels())}")
        if good_offspring(offspringA, population) and good_offspring(
            offspringB, population
        ):
            offspring.append(offspringA)
            offspring.append(offspringB)

        # Mutate

    population.extend(offspring)
    #print(f"-- Debug: {len(population)}")
    #print("----------- PRE SORT ------------")
    #for area in population:
    #    print(f"-- -- Debug: {area}")
    population.sort(key=lambda x: x.get_fitness())
    #print("----------- POST SORT -----------")
    #for area in population:
    #    print(f"-- -- Debug: {area}")
    new_population = population[: int(len(population) / 2)]
    #print("----------- NEW POP  -----------")
    #for area in new_population:
    #    print(f"-- -- Debug: {area}")
    return new_population


def good_offspring(offspring, population):
    good = True
    for area in population:
        if area.get_city_labels() == offspring.get_city_labels():
            good = False
    return good
