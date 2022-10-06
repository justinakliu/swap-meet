import pytest
from swap_meet.item import Item  # may need to delete?
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics
from swap_meet.vendor import Vendor
import time

# `Item`s have age

# Add an `age` attribute to all `Item`s

# Implement a `Vendor` method named `swap_by_newest`, using any logic that seems appropriate

# CLARIFYING QUESTIONS:

# 1 Year/Date/Int: does this require the time library or is age just an integer?
# 2 Unknown or None age? How do we handle that?
# 3 if this is age by date, we need to return an integer to sort?
# 4 How do we want to return the value? With a string output __str__ or in list?
# 5 Can we use helper functions
# 6 Can you return a list sorted by date/age
# 7 Do we want to swap by age + category and/or age + time? Can we make this versatile?

# INPUTS/OUTPUTS:


# PSEUDOCODE:


# @pytest.mark.skip
def test_get_newest():

# ARRANGE
    item_a = Clothing(age=5)
    item_b = Decor(age=19)
    item_c = Electronics(age=.5)
    item_d = Decor(age=123)
    item_e = Electronics(age=33)
    item_f = Clothing(age=9)
    tai = Vendor(inventory=[item_a, item_b, item_c])
    jesse = Vendor(inventory=[item_d, item_e, item_f])
# ACT
    tai_newest = tai.get_by_newest()
    jesse_newest = jesse.get_by_newest()
# ASSERT
    assert tai_newest == item_c
    assert jesse_newest == item_f

@pytest.mark.skip
def test_pass_valid_age_in():
    pass
# ARRANGE
    Variable = 77
    item_a = Clothing(age=None)
    item_b = Decor(age="5")
    item_c = Electronics(age=".5")
    item_d = Decor(age="Hello!")
    item_e = Electronics(age=None)
    item_f = Clothing(age=Variable)
    tai = Vendor(inventory=[item_a, item_b, item_c])
    jesse = Vendor(inventory=[item_d, item_e, item_f])
# ACT
    tai = tai.swap_by_age()
    jesse = jesse.swap_by_age()
# ASSERT
     

@pytest.mark.skip
def test_get_swap_by_age():
    pass
# ARRANGE

# ACT

# ASSERT
