from integration_differentiation import differentiation, integration
from tokenizef import get_tokens, get_constant_power, generate_equation
from get_normal_tangent_pb import (
    get_highest_power,
    line_yintercept,
    get_tangent,
    get_normal,
    get_pb,
)
from get_intercept import (
    quadratic_roots,
    smallest_x_intercept,
    newton_step,
    newton_raphson_approximation,
    get_x_y_intercept,
)


def max_or_min(constants, powers, tp_x):
    max = True
    diff1_c, diff1_p = differentiation(constants, powers)
    diff2_c, diff2_p = differentiation(diff1_p, diff1_c)
    fx = generate_equation(diff2_c, diff2_p)
    max_min = fx(tp_x)

    if max_min > 0:
        max = False

    return max


def complete_the_square(constants):
    x = ((constants[1] / (constants[0]) * 2)) * -1
    y = ((constants[2] / constants[0]) - (x ** 2)) * constants[0]
    return x, y


def get_turning_point(constants, powers):
    x_turning_points = []
    y_turning_points = []

    if get_highest_power(powers) == 2:
        x, y = complete_the_square(constants)
        x_turning_points.append(x)
        y_turning_points.append(y)

    elif get_highest_power(powers) == 3:
        gradient_constants, gradient_powers = differentiation(constants, powers)
        x1, x2 = quadratic_roots(gradient_constants)
        fx = generate_equation(constants, powers)
        y1 = fx(x1)
        y2 = fx(x2)
        x_turning_points.extend([x1, x2])
        y_turning_points.extend([y1, y2])

    return x_turning_points, y_turning_points


def get_area(constants, powers, x_start, x_end):
    int_constants, int_powers = integration(constants, powers)

    fx = generate_equation(int_constants, int_powers)
    area_start = fx(x_start)
    area_end = fx(x_end)

    total_area = area_end - area_start
    return abs(total_area)


def main():
    pass


if __name__ == "__main__":
    main()
