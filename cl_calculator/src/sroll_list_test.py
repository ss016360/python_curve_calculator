from tkinter import *

formulas = [
    {"name": "Formula 1", "value": "2x + 1"},
    {"name": "Formula 2", "value": "2x + 3"},
]


top = Tk()

var = StringVar()
var.set("No Formula Loaded")
displayEntry = Label(top, textvariable=var)
displayEntry.pack(side=TOP, fill=X)

scrollbar = Scrollbar(top)
scrollbar.pack(side=RIGHT, fill=Y)

Lb1 = Listbox(top, yscrollcommand=scrollbar.set)
for formula in formulas:
    Lb1.insert(END, formula["name"])

Lb1.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=Lb1.yview)


def loadFormula(selection):
    selectedFormula = formulas[selection[0]]
    var.set(f"Loaded formula: {selectedFormula['name']} -> {selectedFormula['value']}")


btn1 = Button(
    top, text="Show Selected", command=lambda: loadFormula(Lb1.curselection())
)
btn1.pack()

top.mainloop()
