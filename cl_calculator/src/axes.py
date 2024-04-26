from tkinter import Tk, Canvas, mainloop
from any_power import polynomial
from scale import get_fixed_scale_values, get_y_scale, get_x_scale

# from graph_scale import limits
from tokenizef import (
    contains_number,
    get_tokens,
    get_constant_power,
    generate_equation,
    string_constant_power,
)


def draw_lines(
    canvas,
    x1,
    x2,
    y1,
    y2,
    x_start,
    x_end,
    x_tk_start,
    x_tk_end,
    y_start,
    y_end,
    y_tk_start,
    y_tk_end,
    polynomial,
):
    """draw_lines takes the values of the x and y axes
    getting the values of each axes by having the the start
    and end values then draws the line."""

    tokens = get_tokens(polynomial)
    constants, powers = get_constant_power(tokens)

    # x_start, x_end, y_start, y_end = limits(constants, powers, polynomial)

    canvas.create_line(
        get_x_scale(x1, x_start, x_end, x_tk_start, x_tk_end),
        get_y_scale(y1, y_start, y_end, y_tk_start, y_tk_end),
        get_x_scale(x2, x_start, x_end, x_tk_start, x_tk_end),
        get_y_scale(y2, y_start, y_end, y_tk_start, y_tk_end),
        width=2,
        fill="green",
    )


def indent(
    canvas,
    x1,
    x2,
    y1,
    y2,
    x_start,
    x_end,
    x_tk_start,
    x_tk_end,
    y_start,
    y_end,
    y_tk_start,
    y_tk_end,
    polynomial,
):
    """indent takes in the values of the axis, figuring
    out wether its a y or x axis then drawing indents
    along said axis at intervals as well as stating
    the current values underneath"""

    if int(y1) == 0:
        skipx = round((int(x2) / 5), 0)
        for x in range(int(x1), (int(x2) + 1), 2):
            draw_lines(
                canvas,
                x,
                x,
                0,
                -0.3,
                x_start,
                x_end,
                x_tk_start,
                x_tk_end,
                y_start,
                y_end,
                y_tk_start,
                y_tk_end,
                polynomial,
            )
            canvas.create_text(
                get_x_scale(x, x_start, x_end, x_tk_start, x_tk_end),
                get_y_scale(-0.5, y_start, y_end, y_tk_start, y_tk_end),
                text=str(x),
                fill="green",
            )

    if int(x1) == 0:
        for y in range(int(y1), (int(y2) + 1), 2):
            draw_lines(
                canvas,
                0,
                -0.15,
                y,
                y,
                x_start,
                x_end,
                x_tk_start,
                x_tk_end,
                y_start,
                y_end,
                y_tk_start,
                y_tk_end,
                polynomial,
            )
            canvas.create_text(
                get_x_scale(-0.5, x_start, x_end, x_tk_start, x_tk_end),
                get_y_scale(y, y_start, y_end, y_tk_start, y_tk_end),
                text=str(y),
                fill="green",
            )


def main():
    root = Tk()
    canvas = Canvas(width=1000, height=1000, bg="lightblue")
    canvas.grid()

    polynomial = "3x^2 - 5x + 3"
    x_tk_start = 100
    x_tk_end = 700
    x_start = -5
    x_end = 5

    y_tk_start = 100
    y_tk_end = 700
    y_start = -5
    y_end = 5

    draw_lines(
        canvas,
        x_start,
        x_end,
        0,
        0,
        x_start,
        x_end,
        x_tk_start,
        x_tk_end,
        y_start,
        y_end,
        y_tk_start,
        y_tk_end,
        polynomial,
    )
    draw_lines(
        canvas,
        0,
        0,
        y_start,
        y_end,
        x_start,
        x_end,
        x_tk_start,
        x_tk_end,
        y_start,
        y_end,
        y_tk_start,
        y_tk_end,
        polynomial,
    )

    indent(
        canvas,
        x_start,
        x_end,
        0,
        0,
        x_start,
        x_end,
        x_tk_start,
        x_tk_end,
        y_start,
        y_end,
        y_tk_start,
        y_tk_end,
        polynomial,
    )
    indent(
        canvas,
        0,
        0,
        y_start,
        y_end,
        x_start,
        x_end,
        x_tk_start,
        x_tk_end,
        y_start,
        y_end,
        y_tk_start,
        y_tk_end,
        polynomial,
    )
    mainloop()


if __name__ == "__main__":
    main()
