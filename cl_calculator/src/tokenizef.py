"""
x = -b + math.sqrt(b^2 - 4ac) / 2a
x = -b - math.sqrt(b^2 - 4ac) / 2a
"""

# ?
# * per https://en.wikipedia.org/wiki/Quadratic_formula it seems has only *3* tokens/members at the left of the equal
"""
ax^2       + bx + c = 0
ax^2 + ... + bx + c = 0 # can it have multiple (undetermined ) tokens/members at the left of the equal ?
"""
"""Asking about direction what I plan to do after I finish this problem"""


def contains_number(s):
    """contains_numbers checks wether the argument is a number or not"""
    try:
        float(s)
        return True
    except:
        return False


def get_tokens(formula):
    """get_tokens puts the sign + or - next to the token"""
    tokenized = []
    tokens = formula.split(" ")

    for token in tokens:
        if token == "+" or token == "-":
            sign = token
        elif token[0] == "+" or token[0] == "-":
            tokenized.append(token)
        elif tokens.index(token) == 0:
            tokenized.append("+" + token)
        else:
            tokenized.append(sign + token)

    return tokenized


def get_constant_power(tokens):
    """get_constant_power puts the powers and constant
    of each token into a list and return them"""
    constants = []
    powers = []

    for token in tokens:
        if "x" in token:
            temp = token.split("x")
            if contains_number(temp[0]):
                constants.append(float(temp[0]))
            elif "+" in temp[0]:
                constants.append(1)
            elif "-" in temp[0]:
                constants.append(-1)

            if "^" in temp[1]:
                temp2 = temp[1].split("^")
                if contains_number(temp2[1]):
                    powers.append(float(temp2[1]))
            else:
                powers.append(1)
        elif contains_number(token):
            constants.append(float(token))
            powers.append(0)

    return constants, powers


def generate_equation(constants, powers):
    """equation gets each constant and power from the
    lists as well as the x value to get the y value"""

    def equation(x):
        y = 0
        for constant in range(0, len(constants)):
            c = constants[constant]
            p = powers[constant]

            if p == 0:
                y += c
            else:
                if x == 0 and p < 0:
                    y += 0
                else:
                    y += c * (x ** p)

        return y

    return equation


def string_constant_power(constants, powers):
    formula = ""

    for p in range(0, len(powers)):
        if p == 0:
            if powers[p] == 0:
                formula += str(constants[p])
            elif constants[p] == 1 and powers[p] != 0:
                formula += "x" + "^" + str(powers[p])
            elif constants[p] == -1 and powers[p] != 0:
                formula += "-x" + "^" + str(powers[p])
            else:
                formula += str(constants[p]) + "x^" + str(powers[p])
        elif constants[p] == 1 and powers[p] != 0:
            formula += " " + "+" + " " + "x" + "^" + str(powers[p])
        elif constants[p] == -1 and powers[p] != 0:
            formula += " " + "-" + " " + "x" + "^" + str(powers[p])
        else:
            if constants[p] < 0:
                tempstr1 = str(constants[p])[0]
                tempstr2 = str(constants[p])[1:]
                formula += " " + tempstr1 + " " + tempstr2
                if powers[p] != 0:
                    formula += "x" + "^" + str(powers[p])
            elif constants[p] > 0:
                formula += " " + "+" + " " + str(constants[p])
                if powers[p] != 0 and powers[p] != 1:
                    formula += "x" + "^" + str(powers[p])
                elif powers[p] == 1:
                    formula += "x"
    return formula


def main():
    formula = "5x^3 + 4x^2 - 4x - 4"

    tokens = get_tokens(formula)
    constants, powers = get_constant_power(tokens)

    fx = generate_equation(constants, powers)
    y = fx(1)

    print(formula)
    print(get_tokens(formula))
    print(get_constant_power(tokens))
    print(y)


if __name__ == "__main__":
    main()
