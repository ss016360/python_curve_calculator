from tokenizef import get_tokens, get_constant_power, generate_equation
from get_coordinates import get_coordinates
from get_normal_tangent_pb import (
    get_highest_power,
    line_yintercept,
    get_tangent,
    get_normal,
    get_pb,
)
from get_coordinates import get_coordinates
from tokenizef import get_tokens, get_constant_power, generate_equation
from integration_differentiation import differentiation, integration
import math

"""
Return false for the quadratic if it doesn't intercept the x axis
"""


def quadratic_roots(constants):
    val1 = (constants[1] ** 2) - (4 * constants[0] * constants[2])
    val2 = (constants[1] ** 2) - (4 * constants[0] * constants[2])
    x1 = 0
    x2 = 0
    value = True

    try:
        x1 = (
            -constants[1]
            + math.sqrt((constants[1] ** 2) - (4 * constants[0] * constants[2]))
        ) / (2 * constants[0])
    except ValueError:
        value = False

    try:
        x2 = (
            -constants[1]
            - math.sqrt((constants[1] ** 2) - (4 * constants[0] * constants[2]))
        ) / (2 * constants[0])
    except ValueError:
        value = False

    return x1, x2, value


def smallest_x_intercept(x_start, x_end, y_start, y_end, formula):
    x_coordinates, y_coordinates = get_coordinates(
        x_start,
        x_end,
        y_start,
        y_end,
        formula,
    )
    x = 0
    y = 0
    small = False
    while small == False:
        for i in range(0, len(y_coordinates)):
            if y_coordinates[i] < 1 and y_coordinates[i] > -1:
                x = x_coordinates[i]
                y = y_coordinates[i]
                small = True

    return x, y


def newton_step(f, f_prime, x, tol):
    """
    f is the function
    f_prime is the derivative
    x is the inital guess
    tol is the tolerance
    """
    if abs(f(x)) < tol:
        return x
    else:
        return newton_step(f, f_prime, x - f(x) / f_prime(x), tol)


def newton_raphson_approximation(constants, powers, x, tol=0.0000000000001):
    fx = generate_equation(constants, powers)
    constants_prime, powers_prime = differentiation(powers, constants)
    fx_prime = generate_equation(constants_prime, powers_prime)
    approximate_x = newton_step(fx, fx_prime, x, tol)
    corresponding_y = fx(approximate_x)
    return approximate_x, corresponding_y


def get_x_y_intercept(constants, powers, x_start, x_end, y_start, y_end, formula):
    """
    Figure out what to do when there is not intercept
    """
    yvalue = True
    xvalue = True
    fx = generate_equation(constants, powers)
    try:
        y_intercept = [fx(0)]
    except ValueError:
        yvalue = False

    x_intercept = []
    if get_highest_power(powers) == 1:
        x_intercept.append((constants[1] * -1) / constants[0])

    elif get_highest_power(powers) == 2:
        x1, x2, value = quadratic_roots(constants)
        if value != False:
            x_intercept.append([x1, x2])
        else:
            xvalue = False
    else:
        tol = 0.0000000000001
        approx_x, approx_y = smallest_x_intercept(
            x_start, x_end, y_start, y_end, formula
        )
        smallest_x, smallest_y = newton_raphson_approximation(
            constants, powers, approx_x, tol
        )
        x_intercept.append(smallest_x)
    return y_intercept, x_intercept, yvalue, xvalue


def main():
    formula = "20x^2 + 5"
    tokens = get_tokens(formula)
    constants, powers = get_constant_power(tokens)
    fx = generate_equation(constants, powers)
    y = fx(1)

    x_start = -5
    x_end = 5

    y_start = -5
    y_end = 5

    y1, x1, yv, xv = get_x_y_intercept(
        constants, powers, x_start, x_end, y_start, y_end, formula
    )

    x, y = smallest_x_intercept(x_start, x_end, y_start, y_end, formula)
    newton_raphson_approximation(constants, powers, x, tol=0.0000000000001)


if __name__ == "__main__":
    main()
