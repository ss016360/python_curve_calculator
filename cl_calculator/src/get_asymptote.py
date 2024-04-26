from tokenizef import get_tokens, get_constant_power, generate_equation
from get_normal_tangent_pb import (
    get_highest_power,
    line_yintercept,
    get_tangent,
    get_normal,
    get_pb,
)


def exponential_check(powers):
    exponential = False
    if powers[0] >= 0:
        exponential = False
        return exponential
    else:
        exponential = True
        return exponential


def get_a_asymptote(constants, powers):
    is_exponential = exponential_check(powers)
    if is_exponential == True:
        fx = generate_equation(constants, powers)
        asymptote = fx(0)
        return asymptote


def main():
    pass


if __name__ == "__main__":
    main()
