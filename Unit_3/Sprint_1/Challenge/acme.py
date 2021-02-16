import random


class Product:

    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):

        self.name = str(name)
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def name(self):

        return self.name

    def price(self):

        return self.price

    def weight(self):

        return self.weight

    def flammability(self):

        return self.flammability

    def identifier(self):

        return self.identifier

    def stealability(self):

        self.ratio = self.price / self.weight

        if self.ratio < 0.5:
            return 'Not so stealable...'
        elif ((self.ratio >= .5) and (self.ratio < 1)):
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):

        self.mult = self.flammability * self.weight

        if self.mult < 10:
            return '...fizzle.'
        elif ((self.mult >= 10) and (self.mult < 50)):
            return '...boom!'
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):

    def __init__(self, name, price=10, weight=10, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        super().__init__(name, price, weight, flammability, identifier)

    def explode(self):
        return "...it's a glove"

    def punch(self):

        if self.weight < 5:
            return 'That tickles.'
        elif ((self.weight >= 5) and (self.weight < 15)):
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
