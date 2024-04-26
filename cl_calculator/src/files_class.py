from tkinter import *
from create_save import load_data
from tokenizef import *
from os.path import exists


class Files_Window(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)

        self.var = StringVar()
        self.var.set("No Formula Loaded")
        self.lblAnswer = Label(self, text="No Formula Loaded", relief=RAISED)

        displayEntry = Label(self, textvariable=self.var)

        self.frameDisplay = Frame(self)

        scrollbar = Scrollbar(self.frameDisplay)
        self.Lb1 = Listbox(self.frameDisplay, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.Lb1.yview)
        self.Lb1.bind("<<ListboxSelect>>", self.show_selection)

        self.parent = parent
        self.formulas = []
        self.file_path = "data.json"

        if exists(self.file_path):
            self.formulas = load_data(self.file_path)

        self.reset_listbox()

        self.btnSave_polynomial = Button(
            self, text="Save Polynomial", command=self.Save_polynomial
        )
        self.btnDelete_polynomial = Button(
            self, text="Delete Polynomial", command=self.Delete_polynomial
        )

        self.EnterName = Entry(self)

        self.formulaEntry = Entry(self)

        self.formulaEntry.grid(column=1, row=0)
        self.EnterName.grid(column=0, row=0)
        self.btnSave_polynomial.grid(column=2, row=0)
        displayEntry.grid(column=0, columnspan=3, row=1)
        self.btnDelete_polynomial.grid(column=0, row=2)

        scrollbar.pack(side=RIGHT, fill=Y)
        self.Lb1.pack(side=LEFT, fill=BOTH)
        self.frameDisplay.grid(column=0, columnspan=3, row=3)
        self.lblAnswer.grid(column=2, columnspan=3, row=3)

        self.lblAnswer.config(text=str(self.Lb1.curselection()))

    def reset_listbox(self):
        # Clear the listbox
        self.Lb1.delete(0, self.Lb1.size() - 1)
        # Repopulate the listbox
        for formula in self.formulas:
            self.Lb1.insert(END, formula["name"])

    def show_selection(self, event):
        # self.lb1.curselection() => [0]
        if len(self.Lb1.curselection()) == 0:
            return
        selected = self.Lb1.curselection()[0]
        valueToLoad = self.formulas[selected]
        # self.var.set() - possible option for display entry
        self.lblAnswer.config(text=valueToLoad["formula"])
        # Update the entries to show the loaded formula

    def Save_polynomial(self):
        from create_save import (
            format_data,
            load_data,
            save_data,
            remove_formula_by_name,
            search_dictionary,
        )

        formulaText = self.formulaEntry.get()
        name = str(self.EnterName.get())
        location = search_dictionary(name, self.formulas)
        # print("empty: ", empty, " name: ", name, " formula: ", formulaText)

        if location == -1:
            data_list = [name, formulaText]
            format_data(data_list, self.formulas)
            save_data(self.file_path, self.formulas)
            """ The data if clicked more than once is always saved only two times
            I cannot figure pout why"""

        elif location >= 0:
            """highlight the already existing file and print a
            statement on the screen that the file already exists"""
            self.Lb1.activate(location)
            "this doesn't work"

        self.reset_listbox()

    def Delete_polynomial(self):
        from create_save import (
            format_data,
            load_data,
            save_data,
            remove_formula_by_name,
            search_dictionary,
        )

        delete = self.Lb1.get(
            self.Lb1.curselection()
        )  # to figure out what has been selected from the listbox
        self.formulas = remove_formula_by_name(self.formulas, delete)
        save_data(self.file_path, self.formulas)

        self.reset_listbox()
        """
        I must select something twice in order to delete it"""

    def set_equation(self, formula):
        self.formulaEntry.delete(0, END)
        self.formulaEntry.insert(0, formula)


def main():

    root = Tk()
    root.wm_title("cl_calculator")
    root.geometry("640x480")
    fw = Files_Window(root)
    fw.pack(side="top", fill=BOTH, expand=True)
    root.mainloop()

    # x_start = -5
    # x_end = 5

    # y_start = -5
    # y_end = 5


if __name__ == "__main__":
    main()
