#! /usr/bin/env python

import matplotlib.pyplot as plt
import sys
from time import sleep

from tsp import spawn_population, get_best_area, evolve


def display(area, i):
    print(f"Display: {area}")
    plt.clf()
    loc_x = [a.loc[0] for a in area.cities]
    loc_y = [a.loc[1] for a in area.cities]
    plt.scatter(loc_x, loc_y, marker="o", s=30, color="blue")
    for i in range(len(area.cities) - 1):
        plt.plot(
            [area.cities[i].loc[0], area.cities[i + 1].loc[0]],
            [area.cities[i].loc[1], area.cities[i + 1].loc[1]],
            "ro-",
        )
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.grid()
    plt.text(0.05, 10.8, f"Generation: {i}", fontsize=14)
    plt.text(0.05, 10.2, f"Fitness: {area.get_fitness()}", fontsize=14)
    plt.subplots_adjust(top=0.9)
    plt.show(block=False)
    plt.pause(1)


def main():
    population = spawn_population(10)
    for area in population:
        print(area.get_city_labels())
    ITERATIONS = 10
    for i in range(ITERATIONS):
        print(f"Generation {i}")
        print(population[0])
        for area in population:
            print(area)
        area = get_best_area(population)
        display(area, i)
        population = evolve(population)
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
