import sys

sys.path.append("./src")
from tkinter import Tk, Canvas, mainloop
from src import axes, any_power


def main():
    root = Tk()
    canvas = Canvas(width=1000, height=1000, bg="lightblue")
    canvas.grid()

    x_tk_start = 100
    x_tk_end = 700
    x_start = -5
    x_end = 5

    y_tk_start = 100
    y_tk_end = 700
    y_start = -5
    y_end = 5

    formula = "50x - 90"

    axes.draw_lines(
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
    )
    axes.draw_lines(
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
    )

    axes.indent(
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
    )
    axes.indent(
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
    )

    any_power.polynomial(
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
