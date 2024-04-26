from tokenizef import get_tokens, get_constant_power, generate_equation


def differentiation(constants, powers):
    fx_powers = []
    fx_constant = []

    for p in range(0, len(powers)):
        power = powers[p] - 1
        fx_powers.append(power)
        fx_constant.append(constants[p] * powers[p])

    return fx_constant, fx_powers


def integration(constants, powers):
    fx_powers = []
    fx_constant = []

    for p in range(0, len(powers)):
        power = powers[p] + 1
        fx_powers.append(power)
        fx_constant.append(constants[p] / power)

    return (
        fx_constant,
        fx_powers,
    )


def main():
    from tokenizef import get_constant_power, get_tokens, generate_equation

    formula = "3x^2 + 4x + 2"
    tokens = get_tokens(formula)
    constants, powers = get_constant_power(tokens)

    dif_constant, dif_powers = differentiation(constants, powers)
    int_constant, int_powers = integration(constants, powers)

    print("Normal consant and powers: ", constants, powers)
    print("Differentiatied constants and powers: ", dif_constant, dif_powers)
    print("Integrated constants and powers: ", int_constant, int_powers)


if __name__ == "__main__":
    main()
