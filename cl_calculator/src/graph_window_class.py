from textwrap import fill
from tkinter import *
from tokenizef import *


class GraphWindow(
    Frame,
):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.parent = parent

        self.canvas = Canvas(self, width=1000, height=1000, bg="lightblue")
        self.canvas.pack()
        self.canvas.create_text(730, 400, fill="green", text="x axis")
        self.canvas.create_text(400, 80, fill="green", text="y axis")

        self.equation = ""
        quit = Button(self, text="Quit", command=self.quit)
        quit.place(x=100, y=10)

    def draw_graph(
        self,
        x_start=-20,
        x_end=20,
        x_tk_start=100,
        x_tk_end=700,
        y_start=-40,
        y_end=40,
        y_tk_start=700,
        y_tk_end=100,
    ):
        from any_power import draw_polynomial, polynomial
        from axes import draw_lines, indent

        tokens = get_tokens(self.equation)
        constants, powers = get_constant_power(tokens)

        polynomial(
            self.canvas,
            self.equation,
            x_start,
            x_end,
            x_tk_start,
            x_tk_end,
            y_start,
            y_end,
            y_tk_start,
            y_tk_end,
        )

        draw_lines(
            self.canvas,
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
            self.equation,
        )
        draw_lines(
            self.canvas,
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
            self.equation,
        )

        indent(
            self.canvas,
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
            self.equation,
        )
        indent(
            self.canvas,
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
            self.equation,
        )

    def handle_closeGraph(self):
        self.destroy()

    def setEquation(self, equation):
        self.equation = equation


def main():
    pass


if __name__ == "__main__":
    main()
