from tkinter import *
from any_power import polynomial
from files_class import Files_Window
from graph_window_class import GraphWindow

"""
Show certain buttons based on the highest/lowest power of the polynomial
and wether or not it is a fraction
"""


class MainWindow(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)

        self.parent = parent

        self.extra_inputs = []
        self.clicks = {
            "area": 0,
            "max/min turning point": 0,
            "tangent": 0,
            "normal": 0,
            "perpendicular bisector": 0,
            "x/y intercept": 0,
            "lines intersect": 0,
        }

        btnIntegration = Button(self, text="Integrate", command=self.Integration)
        btnDifferentiation = Button(
            self, text="Differentiate", command=self.Differentiation
        )
        btnTurningPoint = Button(
            self, text="Curve Turning Point", command=self.TurningPoint
        )
        self.btnArea = Button(
            self,
            text="Enter x start and end values for the area",
            command=self.Area,
        )
        self.btnMaxMin_TP = Button(
            self,
            text="Enter the x coordinate for the cubic turning point",
            command=self.MaxMin_TP,
        )
        btnComplete_the_Square = Button(
            self, text="Complete the Square", command=self.Complete_the_Square
        )
        self.btnTangent = Button(
            self,
            text="Enter x and y co-ordinates for the tangent",
            command=self.Tangent,
        )
        self.btnNormal = Button(
            self, text="Enter x and y co-ordinates for the normal", command=self.Normal
        )
        self.btnPB = Button(
            self,
            text="Enter the begining and end co-ordinates for the perpendicular bisector",
            command=self.PB,
        )
        self.btnXY_Intercept = Button(
            self,
            text="Enter graph x and y axis range for the intercept",
            command=self.XY_Intercept,
        )
        btnAsymptote = Button(self, text="Asymptote", command=self.Asymptote)
        self.btnLinesIntersect = Button(
            self,
            text="Enter the graph x and y axis range and second polynomial for where both lines intersect",
            command=self.LinesIntersect,
        )
        btn_showGraph = Button(
            self, text="show polynomial", command=self.handle_showGraph
        )
        btn_delete_answer = Button(self, text="delete", command=self.btn_delete_answer)
        btn_save_answer = Button(self, text="save answer", command=self.handle_saveFile)
        self.lblAnswer = Label(self, text=" ", relief=RAISED)

        # btn_showGraph.grid()

        self.formulaEntry = Entry(self)
        self.formulaEntry_lbl = Label(
            self, text="Enter the formula (e.g. 3x^2 - 0x^2 - 8x + 6): ", relief=RAISED
        )

        self.formulaEntry.grid(row=0, column=2)
        self.lblAnswer.grid(row=1, column=2)
        self.formulaEntry_lbl.grid(row=0, column=1)

        btnIntegration.grid(row=2, column=1)
        btnDifferentiation.grid(row=2, column=2)
        btnTurningPoint.grid(row=2, column=3)
        self.btnArea.grid(row=3, column=1)
        self.btnMaxMin_TP.grid(row=3, column=2)
        btnComplete_the_Square.grid(row=3, column=3)
        self.btnTangent.grid(row=4, column=1)
        self.btnNormal.grid(row=4, column=2)
        self.btnPB.grid(row=4, column=3)
        self.btnXY_Intercept.grid(row=5, column=1)
        btnAsymptote.grid(row=5, column=2)
        self.btnLinesIntersect.grid(row=5, column=3)
        btn_delete_answer.grid(row=6, column=1)
        btn_showGraph.grid(row=6, column=2)
        btn_save_answer.grid(row=6, column=3)

    def create_extra_inputs(self, num_imputs, lbl_list):
        for e in self.extra_inputs:
            e.grid_forget()

        self.LBL_list = []
        for n in self.LBL_list:
            n.grid_forget()

        self.extra_inputs = []
        for i in range(num_imputs):
            extra_lbl = Label(self, text=lbl_list[i - 1])
            extra_input = Entry(self)
            extra_lbl.grid()
            extra_input.grid()
            self.LBL_list.append(extra_lbl)
            self.extra_inputs.append(extra_input)

        return self.extra_inputs

    def show_answer(self, answer):
        self.lblAnswer.config(text=answer)

    def btn_reset_buttons(self):
        self.btnArea.config(text="Enter x start and end values for the area")
        self.clicks["area"] = 0
        self.btnArea.config(text="Enter the x coordinate for the cubic turning point")
        self.clicks["max/min turning point"] = 0
        self.btnTangent.config(text="Enter x and y co-ordinates for the tangent")
        self.clicks["tangent"] = 0
        self.btnNormal.config(text="Enter x and y co-ordinates for the normal")
        self.clicks["normal"] = 0
        self.btnPB.config(
            text="Enter the begining and end co-ordinates for the perpendicular bisector"
        )
        self.clicks["perpendicular bisector"] = 0
        self.btnXY_Intercept.config(
            text="Enter graph x and y axis range for the intercept"
        )
        self.clicks["x/y intercept"] = 0
        self.btnLinesIntersect.config(
            text="Enter the graph x and y axis range and second polynomial for where both lines intersect"
        )
        self.clicks["lines intersect"] = 0

    def btn_delete_answer(self):
        self.show_answer(" ")
        num = len(self.extra_inputs)
        self.formulaEntry.delete(0, END)

        for e in self.extra_inputs:
            e.grid_forget()
        for n in self.LBL_list:
            n.grid_forget()

        self.btn_reset_buttons()
        if num > 0:
            for i in range(0, num):
                self.extra_inputs[i].delete(0, END)

    def Integration(self):
        from integration_differentiation import integration
        from tokenizef import (
            get_tokens,
            get_constant_power,
            generate_equation,
            string_constant_power,
        )

        self.btn_reset_buttons()
        formulaText = self.formulaEntry.get()  # This returns the value
        constants, powers = get_constant_power(get_tokens(formulaText))
        intC, intP = integration(constants, powers)
        integrated_polynomial = string_constant_power(intC, intP)
        self.show_answer(integrated_polynomial)

    def Differentiation(self):
        from integration_differentiation import differentiation
        from tokenizef import (
            get_tokens,
            get_constant_power,
            generate_equation,
            string_constant_power,
        )

        self.btn_reset_buttons()
        formulaText = self.formulaEntry.get()
        constants, powers = get_constant_power(get_tokens(formulaText))
        diffC, diffP = differentiation(constants, powers)
        differentiated_polynomial = string_constant_power(diffC, diffP)
        self.show_answer(differentiated_polynomial)

    def TurningPoint(self):
        from get_tp_area_as import get_turning_point
        from tokenizef import (
            get_tokens,
            get_constant_power,
            generate_equation,
            string_constant_power,
        )

        self.btn_reset_buttons()
        formulaText = self.formulaEntry.get()
        constants, powers = get_constant_power(get_tokens(formulaText))
        tpX, tpY = get_turning_point(constants, powers)
        self.show_answer(
            (
                "x-turning points: ("
                + str(tpX)
                + "), y-turning points: ("
                + str(tpY)
                + ")"
            )
        )

    def Area(self):
        from get_tp_area_as import get_area
        from tokenizef import (
            get_tokens,
            get_constant_power,
            generate_equation,
            string_constant_power,
        )

        if self.clicks["area"] == 0:
            self.btn_reset_buttons()
            self.btnArea.config(text="Calculate Area Underneath Curve")
            extra_lbl = ["x_start: ", "x_end: "]
            self.extra_inputs = self.create_extra_inputs(2, extra_lbl)
        elif self.clicks["area"] > 0:
            formulaText = self.formulaEntry.get()
            x_start = float(self.extra_inputs[0].get())
            x_end = float(self.extra_inputs[1].get())
            constants, powers = get_constant_power(get_tokens(formulaText))
            area = get_area(constants, powers, x_start, x_end)
            self.show_answer(
                "The area between "
                + str(x_start)
                + " and "
                + str(x_end)
                + ": "
                + str(area)
            )
        self.clicks["area"] += 1

    def MaxMin_TP(self):
        from get_tp_area_as import max_or_min
        from tokenizef import (
            get_tokens,
            get_constant_power,
            generate_equation,
            string_constant_power,
        )

        if self.clicks["max/min turning point"] == 0:
            self.btn_reset_buttons()
            self.btnMaxMin_TP.config(text="Calculate Cubic Max or Min Turning Point")
            extra_lbl = ["the x turning point coordinate: "]
            self.extra_inputs = self.create_extra_inputs(1, extra_lbl)
        elif self.clicks["max/min turning point"] > 0:
            formulaText = self.formulaEntry.get()
            tp_x = float(self.extra_inputs[0].get())
            constants, powers = get_constant_power(get_tokens(formulaText))
            max = max_or_min(constants, powers, tp_x)
            if max == True:
                self.show_answer("It is a max turning point")
            else:
                self.show_answer("It is a min turning point")
        self.clicks["max/min turning point"] += 1

    def Complete_the_Square(self):
        from get_tp_area_as import complete_the_square
        from tokenizef import (
            get_tokens,
            get_constant_power,
            generate_equation,
            string_constant_power,
        )

        self.btn_reset_buttons()
        formulaText = self.formulaEntry.get()
        constants, powers = get_constant_power(get_tokens(formulaText))
        x, y = complete_the_square(constants)
        self.show_answer("x turning point: " + str(x) + "y turning point: " + str(y))

    def Tangent(self):
        from get_normal_tangent_pb import get_tangent
        from tokenizef import (
            get_tokens,
            get_constant_power,
            generate_equation,
            string_constant_power,
        )

        if self.clicks["tangent"] == 0:
            self.btn_reset_buttons()
            self.btnTangent.config(text="Calculate Tangent")
            extra_lbl = ["the x coordinate: ", "the y coordinate: "]
            self.extra_inputs = self.create_extra_inputs(2, extra_lbl)
        elif self.clicks["tangent"] >= 1:
            formulaText = self.formulaEntry.get()
            constants, powers = get_constant_power(get_tokens(formulaText))
            x = float(self.extra_inputs[0].get())
            y = float(self.extra_inputs[1].get())
            m, t_constants, t_powers = get_tangent(constants, powers, x, y)
            t_formula = string_constant_power(t_constants, t_powers)
            self.show_answer(
                "tangent gradient: " + str(m) + "tangent formula: " + t_formula
            )
        self.clicks["tangent"] += 1

    def Normal(self):
        from get_normal_tangent_pb import get_normal
        from tokenizef import (
            get_tokens,
            get_constant_power,
            generate_equation,
            string_constant_power,
        )

        if self.clicks["normal"] == 0:
            self.btn_reset_buttons()
            self.btnNormal.config(text="Calculate Normal")
            extra_lbl = ["the x coordinate: ", "the y coordinate: "]
            self.extra_inputs = self.create_extra_inputs(2, extra_lbl)
        elif self.clicks["normal"] >= 1:
            formulaText = self.formulaEntry.get()
            constants, powers = get_constant_power(get_tokens(formulaText))
            x = float(self.extra_inputs[0].get())
            y = float(self.extra_inputs[1].get())
            n_constants, n_powers = get_normal(constants, powers, x, y)
            n_formula = string_constant_power(n_constants, n_powers)
            self.show_answer("normal formula: " + n_formula)
        self.clicks["normal"] += 1

    def PB(self):
        from get_normal_tangent_pb import get_pb
        from tokenizef import (
            get_tokens,
            get_constant_power,
            generate_equation,
            string_constant_power,
        )

        if self.clicks["perpendicular bisector"] == 0:
            self.btn_reset_buttons()
            self.btnPB.config(text="Calculate Perpendicular Bisector")
            extra_lbl = [
                "starting x coordinate of the line:",
                "starting y coordinate of the line:",
                "ending x coordinate of the line:",
                "ending y coordinate of the line:",
            ]
            self.extra_inputs = self.create_extra_inputs(4, extra_lbl)
        elif self.clicks["perpendicular bisector"] >= 1:
            formulaText = self.formulaEntry.get()
            constants, powers = get_constant_power(get_tokens(formulaText))
            startx = float(self.extra_inputs[0].get())
            starty = float(self.extra_inputs[1].get())
            endx = float(self.extra_inputs[2].get())
            endy = float(self.extra_inputs[3].get())
            pb_constants, pb_powers = get_pb(
                constants, powers, startx, endx, starty, endy
            )
            pb_formula = string_constant_power(pb_constants, pb_powers)
            self.show_answer("Perpendicular formula: " + pb_formula)
        self.clicks["perpendicular bisector"] += 1

    def XY_Intercept(self):
        from get_intercept import get_x_y_intercept
        from tokenizef import (
            get_tokens,
            get_constant_power,
            generate_equation,
            string_constant_power,
        )

        if self.clicks["x/y intercept"] == 0:
            self.btn_reset_buttons()
            self.btnXY_Intercept.config(text="Calculate the x and y axis intercepts")
            extra_lbl = [
                "start x coordinate: ",
                "start y coordinate: ",
                "end x coordinate: ",
                "end y coordinate: ",
            ]
            self.extra_inputs = self.create_extra_inputs(4, extra_lbl)
        elif self.clicks["x/y intercept"] >= 1:
            formulaText = self.formulaEntry.get()
            constants, powers = get_constant_power(get_tokens(formulaText))
            startx = float(self.extra_inputs[0].get())
            starty = float(self.extra_inputs[1].get())
            endx = float(self.extra_inputs[2].get())
            endy = float(self.extra_inputs[3].get())
            x_intercepts, y_intercepts = get_x_y_intercept(
                constants, powers, startx, endx, starty, endy, formulaText
            )
            string_y_intercepts = ""
            string_x_intercepts = ""
            for y in y_intercepts:
                string_y_intercepts += str(y) + ", "
            for x in x_intercepts:
                string_x_intercepts += str(x) + ", "

            self.show_answer(
                "x axis intercepts: "
                + string_x_intercepts
                + "y axis intercepts: "
                + string_y_intercepts
            )
        self.clicks["x/y intercept"] += 1

    def Asymptote(self):
        from get_asymptote import get_a_asymptote
        from tokenizef import (
            get_tokens,
            get_constant_power,
            generate_equation,
            string_constant_power,
        )

        self.btn_reset_buttons()
        formulaText = self.formulaEntry.get()
        constants, powers = get_constant_power(get_tokens(formulaText))
        asymptote = get_a_asymptote(constants, powers)
        self.show_answer("Asymptote: " + str(asymptote))

    def LinesIntersect(self):
        from get_lines_intersect import get_intersect
        from tokenizef import (
            get_tokens,
            get_constant_power,
            generate_equation,
            string_constant_power,
        )

        if self.clicks["lines intersect"] == 0:
            self.btn_reset_buttons()
            self.btnLinesIntersect.config(text="Calculate where both lines intersect")
            extra_lbl = [
                "polynomial of the second line/curve: ",
                "start x coordinate: ",
                "start y coordinate: ",
                "end x coordinate: ",
                "end y coordinate: ",
            ]
            self.extra_inputs = self.create_extra_inputs(5, extra_lbl)
        elif self.clicks["lines intersect"] >= 1:
            formulaText = self.formulaEntry.get()
            constants1, powers1 = get_constant_power(get_tokens(formulaText))
            formulaText2 = self.extra_inputs[0].get()
            startx = float(self.extra_inputs[1].get())
            starty = float(self.extra_inputs[2].get())
            endx = float(self.extra_inputs[3].get())
            endy = float(self.extra_inputs[4].get())

            constants2, powers2 = get_constant_power(get_tokens(formulaText2))
            x_intercepts, y_intercepts = get_intersect(
                constants1, constants2, powers1, powers2, startx, endx, starty, endy
            )

            string_y_intercepts = ""
            string_x_intercepts = ""
            for y in y_intercepts:
                string_y_intercepts += str(y) + ", "
            for x in x_intercepts:
                string_x_intercepts += str(x) + ", "

            self.show_answer(
                "x intercepts: "
                + string_x_intercepts
                + "y intercepts: "
                + string_y_intercepts
            )
        self.clicks["lines intersect"] += 1

    def handle_showGraph(self):
        graph_tk = Toplevel(self)
        graph_tk.wm_title = "Graph ..."
        graph_window = GraphWindow(graph_tk)
        graph_window.pack(side="top", fill=BOTH, expand=True)
        graph_window.setEquation(self.formulaEntry.get())
        graph_window.draw_graph()

    def handle_saveFile(self):
        saveFile = Toplevel(self)
        saveFile.wm_title = "Save or Load Graphs"
        saveFile_window = Files_Window(saveFile)
        saveFile_window.pack(side="top", fill=BOTH, expand=True)
        saveFile_window.set_equation(self.formulaEntry.get())


def main():

    root = Tk()
    root.wm_title("cl_calculator")
    root.geometry("1410x400")
    # root.attributes("-fullscreen", True)
    mw = MainWindow(root)
    mw.pack(side="top", fill=BOTH, expand=True)
    root.mainloop()

    x_start = -5
    x_end = 5

    y_start = -5
    y_end = 5


if __name__ == "__main__":
    main()
