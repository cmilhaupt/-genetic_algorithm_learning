#! /usr/bin/env python

import matplotlib.pyplot as plt
import sys
from time import sleep, time

from tsp import spawn_population, get_best_area, evolve


def display(area, i):
    print(f"Display: {area}")
    generation = i
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
    plt.text(0.05, 10.8, f"Generation: {generation}", fontsize=14)
    plt.text(0.05, 10.2, f"Fitness: {area.get_fitness()}", fontsize=14)
    plt.subplots_adjust(top=0.9)
    plt.show(block=False)
    plt.pause(0.1)


def main():
    print("Spawning population")
    population = spawn_population(10)
    ITERATIONS = 20
    for i in range(ITERATIONS):
        print(f"Generation {i}")
        #for area in population:
        #    print(area)
        print("Getting best area")
        best_area = get_best_area(population)
        print("Displaying best area")
        display(best_area, i)
        print("Evolving population")
        population = evolve(population)
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
