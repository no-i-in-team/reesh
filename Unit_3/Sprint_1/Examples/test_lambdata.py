"""Basic unit tests for lambda package"""

# from random import randit
import pytest
import lambdata as ld

""" inside pipenv > pytest test_lambdata.py --verbose """

def inc(x):
    return x+1

def test_inc():
    ans = inc(3)
    assert ans == 4
    assert ans == 7

def test_inc_2():
    ans = inc(3)
    ans_2 = inc(6)
    assert ans == 5
    assert ans_2 == 7

def test_increment_int():
    x0 = 0
    y0 = ld.increment(x0) # 1
    assert y0 == 1

def test_increment_float():
    x0 = 10.5
    y0 = ld.increment(x0) # 11.5
    assert y0 == 11.5

def test_increment_neg_int():
    x0 = -2
    y0 = ld.increment(x0) # -1
    assert y0 == -1

def test_increment_neg_float():
    x0 = -2.5
    y0 = ld.increment(x0) # -1.5
    assert yp == -1.5

def test_colors():

    assert "Cyan" in ld.COLORS
    assert "Mauve" in ld.COLORS
    assert "Blue" in ld.COLORS
    assert "Red" not in ld.COLORS

def test_number_colors():

    assert len(ld.COLORS) == 4

user1 = ld.oop_examples.SocialMediaUser(name="Nick", location="Arizona")
user2 = ld.oop_examples.SocialMediaUser(name="Carls", location="Costa Rica",upvotes=250)


def test_SMU_constructor():
    """Testing that SMU constructor works properly"""
    # testing name
    assert user1.name.lower() == "nick"
    assert user2.name.lower() == "carl"
    # testing location
    assert user1.location.lower() == "arizona"
    assert user2.location.lower() == "costa rica"
    # testing upvotes
    assert user1.upvotes == 0
    assert user2.upvotes == 250

def test_unpopular():
    "Testing to make sure 0 upvotes is unpopular"
    assert isinstance(user1.is_popular(), bool)
    assert not user1.is_popular()

def test_popular():
    "Testing to make sure 250 upvotes is popular"
    assert isinstance(user2.is_popular(), bool)
    assert user2.is_popular()

def test_SMU_constructor_types():
    """Testing Types"""
    assert isinstance(user1.name, str)
    assert isinstance(user1.location, str)
    assert isinstance(user1.upvotes, int)