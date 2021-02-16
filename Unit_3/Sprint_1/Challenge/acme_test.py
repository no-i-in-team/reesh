#!/usr/bin/env python

from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


def test_default_product_price():
    """Test default product price being 10."""
    prod = Product('Test Product')
    assert prod.price == 10


def test_default_product_weight():

    prod = Product('Test Product')
    assert prod.weight == 20


def test_methods():

    prod = Product(name='Test Product 1', price=19,
                   weight=190, flammability=0.19)
    assert prod.stealability() == 'Not so stealable...'
    assert prod.explode() == '...boom!'


def test_default_num_products():

    products = generate_products()
    assert isinstance(products, list)
    assert len(products) == 30


def test_legal_names():

    adj = []
    noun = []

    products = generate_products()

    for item in products:
        split = item.name.split(' ')
        adj.append(split[0])
        noun.append(split[1])

    for i in range(len(products)):
        assert adj[i] in ADJECTIVES
        assert noun[i] in NOUNS
