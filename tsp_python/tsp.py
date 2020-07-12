import math
import numpy
import random

from selection import get_parent

class City:
    def __init__(self, x, y, label):
        self.id = label
        self.loc = numpy.array((x, y))

    def distance_to(self, city):
        return numpy.linalg.norm(city.loc - self.loc)

    def __str__(self):
        return f"{self.id}: ({self.loc})"

class Area:
    def __init__(self, cities):
        self.cities = cities

    def get_fitness(self):
        fitness = 0.0
        for i in range(len(self.cities) - 1):
            fitness += self.cities[i].distance_to(self.cities[i+1])
        return fitness
        

def argmax(population):
    score = math.inf
    best = None
    for area in population:
        current = area.get_fitness()
        if current < score:
            best = area
            score = current
    return best

def initialize_areas(num, size=10):
    cities = list()
    for i, _ in enumerate(range(num)):
        x = random.uniform(0, size)
        y = random.uniform(0, size)
        cities.append(City(x, y, i))
    random.shuffle(cities)
    area = Area(cities)
    return area

def spawn_population(num):
    return [initialize_areas(10) for _ in range(num)]

def get_best_area(population):
    #area = argmax(population)
    area = get_parent(population)
    return area

def evolve(population):
    offsprint = list()
    # Get parents
    p1 = get_parent(population)
    p2 = get_parent(population)
    while p1 == p2:
        p2 = get_parent(population)
    # Crossover
    # Mutate
