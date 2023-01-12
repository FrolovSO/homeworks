class Country:
    pass


class Russia(Country):
    def __init__(self, population):
        self.population = population

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        self._population = value


class Canada(Country):
    def __init__(self, population):
        self.population = population

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        self._population = value


class Germany(Country):
    def __init__(self, population):
        self.population = population

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        self._population = value
