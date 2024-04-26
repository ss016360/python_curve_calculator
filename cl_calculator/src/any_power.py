from tkinter import Tk, Canvas, mainloop
from scale import get_fixed_scale_values, get_y_scale, get_x_scale
from get_coordinates import get_coordinates


def draw_polynomial(
    canvas,
    x_start,
    x_end,
    x_tk_start,
    x_tk_end,
    y_start,
    y_end,
    y_tk_start,
    y_tk_end,
    x_coordinates,
    y_coordinates,
):
    """draw_polynomial draws the the polynomial with the coordinates
    given, and makes sure that the same line that goes outside of the
    graph isn't connected by a line at the end of the graph"""
    for i in range(0, len(y_coordinates) - 1):
        if x_coordinates[i + 1] - x_coordinates[i] < 0.02:
            canvas.create_line(
                get_x_scale(x_coordinates[i], x_start, x_end, x_tk_start, x_tk_end),
                get_y_scale(y_coordinates[i], y_start, y_end, y_tk_start, y_tk_end),
                get_x_scale(x_coordinates[i + 1], x_start, x_end, x_tk_start, x_tk_end),
                get_y_scale(y_coordinates[i + 1], y_start, y_end, y_tk_start, y_tk_end),
                width=2,
                fill="blue",
            )


def polynomial(
    canvas,
    formula,
    x_start,
    x_end,
    x_tk_start,
    x_tk_end,
    y_start,
    y_end,
    y_tk_start,
    y_tk_end,
):
    """polynomial gets the the coordinates of the polynomial and draws it"""
    x_coordinates, y_coordinates = get_coordinates(
        x_start,
        x_end,
        y_start,
        y_end,
        formula,
    )
    draw_polynomial(
        canvas,
        x_start,
        x_end,
        x_tk_start,
        x_tk_end,
        y_start,
        y_end,
        y_tk_start,
        y_tk_end,
        x_coordinates,
        y_coordinates,
    )


def main():
    root = Tk()
    canvas = Canvas(width=1000, height=1000, bg="lightblue")
    canvas.grid()

    x_start = -5
    x_end = 5
    x_tk_start = 100
    x_tk_end = 700

    y_start = -5
    y_end = 5
    y_tk_start = 100
    y_tk_end = 700

    formula = "2x^3 + x^2 - 13x + 6"

    polynomial(
        canvas,
        formula,
        x_start,
        x_end,
        x_tk_start,
        x_tk_end,
        y_start,
        y_end,
        y_tk_start,
        y_tk_end,
    )

    mainloop()


if __name__ == "__main__":
    main()
