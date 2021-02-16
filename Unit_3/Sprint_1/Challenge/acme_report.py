#!/usr/bin/env python

from random import randint, uniform, choice
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):

    products = []

    for i in range(num_products):
        name = f'{choice(ADJECTIVES)} {choice(NOUNS)}'
        price = randint(5, 100)
        weight = randint(5, 100)
        flammmability = uniform(0.0, 2.5)
        products.append(Product(name, price, weight, flammmability))
    return products


def inventory_report(products):

    names = set()
    prices = []
    weights = []
    flamm = []

    for item in products:
        names.add(item.name)
        prices.append(item.price)
        weights.append(item.weight)
        flamm.append(item.flammability)

    print(f'Unique prodcut names: {len(names)}')
    print(f'Avergae price: {sum(prices)/len(prices)}')
    print(f'Average weight: {sum(weights)/len(weights)}')
    print(f'Average flammability: {sum(flamm)/len(flamm)}')


if __name__ == '__main__':

    inventory_report(generate_products())
