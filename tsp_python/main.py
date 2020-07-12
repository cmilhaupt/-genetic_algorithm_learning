#! /usr/bin/env python

import matplotlib.pyplot as plt
import sys
from time import sleep

from tsp import spawn_population, get_best_area, evolve

def display(area):
    plt.clf()
    loc_x = [a.loc[0] for a in area.cities]
    loc_y = [a.loc[1] for a in area.cities]
    plt.scatter(loc_x, loc_y, marker='o', s=30, color='blue')
    for i in range(len(area.cities) - 1):
        plt.plot([area.cities[i].loc[0], area.cities[i+1].loc[0]],
                [area.cities[i].loc[1], area.cities[i+1].loc[1]], 'ro-')
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.grid()
    plt.text(.05, 10.4, f"Fitness: {area.get_fitness()}", fontsize=14)
    plt.subplots_adjust(top=0.9)
    plt.show(block=False)
    plt.pause(1)

def main():
    population = spawn_population(100)
    ITERATIONS = 5
    for i in range(ITERATIONS):
        area = get_best_area(population)
        display(area)
        evolve(population)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
