from tokenizef import *
from scale import get_fixed_scale_values, get_y_scale, get_x_scale
from get_intercept import (
    quadratic_roots,
    smallest_x_intercept,
    newton_step,
    newton_raphson_approximation,
    get_x_y_intercept,
)
from get_tp_area_as import max_or_min, complete_the_square, get_turning_point, get_area
from get_normal_tangent_pb import (
    get_highest_power,
    line_yintercept,
    get_tangent,
    get_normal,
    get_pb,
)

"""
write out every single case/possiblity for the turning point
make sure that you do an if statement for if the curve doesn't touch the axes
make sure you figure out the turning points for the quadratic
"""

"""
* -10 -> 10 for both x and y axes as default
* scaling dosnet matter for exponential
* allow someone to enter limits for a scale they want on a graph

1. ALWAYS when the values are outside of the default range to change
the limits so the line/curve fits inside:

2. if where it crosses the x/y axis and/or the max or min turning
points > range then:

3. Is x/y axis or max or min (large or small) (only if the polynomial
has a max or min) then that divided by the default limits so that you
know what to scale by
"""


def repeat_until_value(current, endvalue):
    e = endvalue
    c = current
    if endvalue > c:
        if endvalue > 0:
            while c < (endvalue + (endvalue * 10)):
                c += 1
        elif endvalue < 0:
            while c < (endvalue + (endvalue * -10)):
                c += 1
        elif endvalue == 0:
            c += 10

    elif endvalue < c:
        if endvalue > 0:
            while c > (endvalue - (endvalue * 10)):
                c -= 1
        elif endvalue < 0:
            while c > (endvalue - (endvalue * -10)):
                c -= 1
        elif endvalue == 0:
            c -= 10

    return c


def limits(
    constants,
    powers,
    formula,
    defaultStartX=-10,
    defaultEndX=10,
    defaultStartY=-10,
    defaultEndY=10,
):

    highest_power = get_highest_power(powers)
    StartX = 0
    EndX = 0
    StartY = 0
    EndY = 0

    if highest_power == 1:
        y, x, yvalue, xvalue = get_x_y_intercept(
            constants,
            powers,
            defaultStartX,
            defaultEndX,
            defaultStartY,
            defaultEndY,
            formula,
        )
        val = 1
        while x == 0 and y != 0:
            y, x, yvalue, xvalue = get_x_y_intercept(
                constants,
                powers,
                defaultStartX ** val,
                defaultEndX ** val,
                defaultStartY ** val,
                defaultEndY ** val,
                formula,
            )
            val += 1

        x.append(0)
        y.append(0)

        EndX = max(x) + abs(max(x) * 0.1)
        StartX = min(x) - abs(min(x) * 0.1)

        EndY = max(y) + abs(max(y) * 0.1)
        StartY = min(y) - abs(min(y) * 0.1)

    elif highest_power == 2 or highest_power == 3:
        y_intercept, x_intercept, yvalue, xvalue = get_x_y_intercept(
            constants,
            powers,
            defaultStartX,
            defaultEndX,
            defaultStartY,
            defaultEndY,
            formula,
        )

        y_tp, x_tp = get_turning_point(constants, powers)

        maxX = x_tp[0]
        minX = x_tp[0]
        maxY = y_tp[0]
        minY = y_tp[0]

        for i in range(0, len(y_tp)):
            if y_tp[i] < defaultStartY:
                if y_tp[i] < minY:
                    minY = y_tp[i]
            elif y_tp[i] > defaultEndY:
                if y_tp[i] > maxY:
                    maxY = y_tp[i]

            if x_tp[i] < defaultStartX:
                if x_tp[i] < minX:
                    minX = x_tp[i]
            elif x_tp[i] > defaultEndX:
                if x_tp[i] > maxX:
                    maxX = x_tp[i]

        for i in range(0, len(y_intercept)):
            if y_intercept[i] < defaultStartY:
                if y_intercept[i] < minY:
                    minY = y_intercept[i]
            elif y_intercept[i] > defaultEndY:
                if y_intercept[i] > maxY:
                    maxY = y_intercept[i]

        for i in range(0, len(x_intercept)):
            if x_intercept[i] < defaultStartX:
                if x_intercept[i] < minX:
                    minX = x_intercept[i]
            elif x_intercept[i] > defaultEndX:
                if x_intercept[i] > maxX:
                    maxX = x_intercept[i]

        if maxX > defaultEndX:
            EndX = repeat_until_value(maxX, defaultEndX)
        elif minX < defaultStartX:
            StartX = repeat_until_value(minX, defaultStartX)

        if maxY > defaultEndY:
            EndY = repeat_until_value(maxY, defaultEndY)
        elif minY < defaultStartY:
            StartY = repeat_until_value(minY, defaultStartY)

    StartX += defaultStartX
    EndX += defaultEndX
    StartY += defaultStartY
    EndY += defaultEndY

    return StartX, EndX, StartY, EndY


def main():

    formula = "2x + 100"
    tokens = get_tokens(formula)
    constants, powers = get_constant_power(tokens)
    limits(constants, powers, formula)


if __name__ == "__main__":
    main()
