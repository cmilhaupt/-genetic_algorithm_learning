import numpy


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
            fitness += self.cities[i].distance_to(self.cities[i + 1])
        return fitness
    
    def get_city_labels(self):
        return [str(c.id) for c in self.cities]

    def __len__(self):
        return len(self.cities)

    def __str__(self):
        return f"Area: len(cities)={len(self.cities)}, fitness={self.get_fitness()}"
