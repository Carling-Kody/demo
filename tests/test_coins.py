import pytest
from files.coins import sum_dimes, sum_pennies, sum_nickles, sum_quarters, sum_all_coins


def test_sum_pennies():
    total= sum_pennies(user_input=50)
    assert total == 50


def test_sum_nickles():
    total = sum_nickles(user_input=10)
    assert total == 50


def test_sum_dimes():
    total = sum_dimes(user_input=5)
    assert total == 50


def test_sum_quarters():
    total = sum_quarters(user_input=2)
    assert total == 50


def test_sum_all_coins(pennies=50, nickles=10, dimes=5, quarters=2):
    total = sum_all_coins(pennies, nickles, dimes, quarters)
    assert total == 200


def test_you_win():
    
    pass


def test_over_dollar():
    pass


def test_under_dollar():
    pass

