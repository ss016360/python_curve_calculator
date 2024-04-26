from tokenizef import get_tokens, get_constant_power, generate_equation
from integration_differentiation import differentiation, integration


def get_highest_power(powers):
    highest = powers[0]
    for p in range(0, len(powers)):
        if highest < powers[p]:
            highest = powers[p]

    return highest


def line_yintercept(m, x, y):
    yintercept = (m * (-1 * x)) + y
    return yintercept


def get_tangent(powers, constants, x, y):
    m_constants, m_powers = differentiation(powers, constants)
    t_m = generate_equation(
        m_constants,
        m_powers,
    )
    m = t_m(x)
    yintercept = line_yintercept(m, x, y)

    t_constants = [m, yintercept]
    t_powers = [1, 0]
    return m, t_constants, t_powers


def get_normal(constants, powers, x, y):
    t_m, m_constants, m_powers = get_tangent(constants, powers, x, y)
    n_m = (t_m ** -1) * -1
    yintercept = line_yintercept(n_m, x, y)

    n_constants = [n_m, yintercept]
    n_powers = [1, 0]
    return n_constants, n_powers


def get_pb(powers, constants, startx, endx, starty, endy):
    mid_x = (endx + startx) / 2
    mid_y = (starty + endy) / 2
    pb_constants, pb_powers = get_normal(constants, powers, mid_x, mid_y)

    return pb_constants, pb_powers


def main():
    formula = "5x^3 + 4x^2 - 4x - 4"
    tokens = get_tokens(formula)
    constants, powers = get_constant_power(tokens)


if __name__ == "__main__":
    main()
