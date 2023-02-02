class Country:
    def __init__(self, population):
        self.population = population

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        self._population = value


class Russia(Country):
    pass


class Canada(Country):
    pass


class Germany(Country):
    pass


amount_rus = Russia(200000000)
amount_can = Canada(50000000)
amount_germ = Germany(2000000)
print(amount_rus.population)
print(amount_can.population)
print(amount_germ.population)
