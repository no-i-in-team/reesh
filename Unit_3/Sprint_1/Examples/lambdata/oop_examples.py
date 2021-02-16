"""This an example of OOP inside a module"""

class MyDataFrame(pd.DataFrame):

    def num_cells(self):
        return self.shape[0] * self.shape[1]  # total data points


class BareMinimumClass:
    pass


class Complex:
    def __init__(self, realpart, imagpart=-5):
        """
        Constructor for Complex numbers.
        Complex numbers are part real and part imaginary.
        """
        self.r = realpart
        self.i = imagpart

    def add(self, other_complex):
        """
        Takes another complex number and adds it
        to itself.
        """
        # other_complex = num2
        # self = num1
        self.r += other_complex.r
        self.i += other_complex.i

    def __repr__(self):
        return "({}, i{})".format(self.r, self.i)


class SocialMediaUser:
    def __init__(self, name, location, upvotes=0):
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)

    def recieve_upvotes(self, num_upvotes=1):
        self.upvotes += num_upvotes

    def is_popular(self):
        return self.upvotes > 100


class Animal:
    """General Representation of Animals"""

    def __init__(self, name, weight, location="Earth", diet_type="Food"):
        self.name = name
        self.weight = weight
        self.location = location
        self.diet_type = diet_type

    def eat(self, food):
        return "Huge fan of that " + food

    def run(self):
        return "Vroom, Vroom, I go quick"


class Sloth(Animal):
    def __init__(self, name, weight, location, diet_type, num_naps=160):
        super().__init__(name, weight, location, diet_type)
        self.num_naps = num_naps

    def say_something(self):
        return "This is a sloth of typing"

    def run(self):
        return "I am a slow guy - I dont run"