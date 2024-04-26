import pytest
import get_intercept
from tokenizef import generate_equation


def test_quadratic_roots():
    constants = [6, -10, -4]
    assert get_intercept.quadratic_roots(constants) == (2, -(1 / 3))


def test_smallest_x_intercept():
    formula = "5x^3 + 4x^2 - 4x - 4"
    x_start = -5
    x_end = 5
    y_start = -5
    y_end = 5

    x, y = get_intercept.smallest_x_intercept(x_start, x_end, y_start, y_end, formula)
    assert y < 1
    assert y > -1


def test_newton_raphson_approximation():
    formula = "5x^3 + 4x^2 - 4x - 4"
    x_start = -5
    x_end = 5
    y_start = -5
    y_end = 5

    x, y = get_intercept.smallest_x_intercept(x_start, x_end, y_start, y_end, formula)
    tokens = get_intercept.get_tokens(formula)
    constants, powers = get_intercept.get_constant_power(tokens)
    tol = 0.0000000000001

    approximate_x, corresponding_y = get_intercept.newton_raphson_approximation(
        constants, powers, x, tol
    )
    check_fx = generate_equation(constants, powers)
    check = check_fx(approximate_x)

    assert round(check, 3) == round(corresponding_y, 3)
    assert abs(corresponding_y - 0) < tol


# what do I do to get all of the 3 possible intercepts for the power of 3
def test_get_x_y_intercept():
    x_start = -5
    x_end = 5
    y_start = -5
    y_end = 5

    formula = "x^2 + 4x + 4"
    tokens = get_intercept.get_tokens(formula)
    constants, powers = get_intercept.get_constant_power(tokens)

    line_intercept_y, line_intercept_x = get_intercept.get_x_y_intercept(
        [2, 4], [1, 0], x_start, x_end, y_start, y_end, "2x + 4"
    )
    assert line_intercept_y == [4]
    assert line_intercept_x == [-2]

    quadratic_intercept_y, quadratic_intercept_x = get_intercept.get_x_y_intercept(
        constants, powers, x_start, x_end, y_start, y_end, formula
    )
    assert quadratic_intercept_y == [4]
    assert quadratic_intercept_x == [-2, -2]
