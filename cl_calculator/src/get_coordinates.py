from tokenizef import get_tokens, get_constant_power, generate_equation


def get_coordinates(x_start, x_end, y_start, y_end, formula):
    """get_coordinates takes x and y starting and ending coordinates,
    calculates coordinates that are inside the graph
    and returns them as two lists of values"""
    x_coordinates = []
    y_coordinates = []

    tokens = get_tokens(formula)
    constants, powers = get_constant_power(tokens)
    while x_start <= x_end:
        # maybe y must be replaced with what actually the equation does to x_start
        fx = generate_equation(constants, powers)
        y = fx(x_start)
        if y >= y_start and y <= y_end:
            x_coordinates.append(x_start)
            y_coordinates.append(y)
        # add a really small amount so it looks like a curve
        x_start += 0.01
    return x_coordinates, y_coordinates


def main():
    formula = "3x^2 + 4x + 2"
    x, y = get_coordinates(-5, 5, -5, 5, formula)
    x.sort()
    y.sort()
    print(f"x start: {round(x[0], 3)}, x end: {round(x[-1], 3)}")
    print(f"y start: {round(y[0], 3)}, y end: {round(y[-1], 3)}")


if __name__ == "__main__":
    main()
