import pytest
import get_asymptote


def test_exponential_check():
    powers = [-1, 0]
    assert get_asymptote.exponential_check(powers) == True
    assert get_asymptote.exponential_check([2, 0]) == False


def test_get_a_asymptote():
    powers = [-1, 0]
    constants = [2, 5]
    powers2 = [-2, 1, 0]
    constants2 = [4, 6, 3]
    assert get_asymptote.get_a_asymptote(constants, powers) == 5
    assert get_asymptote.get_a_asymptote(constants2, powers2) == 3
