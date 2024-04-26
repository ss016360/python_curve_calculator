# I would like to use this as a future refrence, there is still some code to be used


def linearInfo():
    linearLabel1 = Label(root, text="gradient: ")
    linearLabel1.place(x=260, y=10)
    linearEntry1 = Entry(root, bd=2)
    linearEntry1.place(x=330, y=10)
    linearLabel2 = Label(root, text="y-intersect: ")
    linearLabel2.place(x=530, y=10)
    linearEntry2 = Entry(root, bd=2)
    linearEntry2.place(x=620, y=10)
    return linearEntry1, linearEntry2


def quadraticInfo():
    quadLabel1 = Label(root, text="a value: ")
    quadLabel1.place(x=150, y=50)
    quadEntry1 = Entry(root, bd=2)
    quadEntry1.place(x=220, y=50)
    quadLabel2 = Label(root, text="b value: ")
    quadLabel2.place(x=420, y=50)
    quadEntry2 = Entry(root, bd=2)
    quadEntry2.place(x=500, y=50)
    quadLabel3 = Label(root, text="c value: ")
    quadLabel3.place(x=700, y=50)
    quadEntry3 = Entry(root, bd=2)
    quadEntry3.place(x=780, y=50)
    return quadEntry1, quadEntry2, quadEntry3


def reset():
    pass


def linearInput():
    linearEntry1, linearEntry2 = linearInfo()
    linearM = float(linearEntry1.get())
    linearC = float(linearEntry1.get())

    for i in range(-17, 17):
        x1 = i
        x2 = x1 + 1
        y1 = (linearM * x1) + linearC
        y2 = (linearM * x2) + linearC
        canvas.create_line(x1, y1, x2, y2, width=3, fill="black")


def quadraticInput():
    quadEntry1, quadEntry2, quadEntry3 = quadraticInfo()
    quadA = float(quadEntry1.get())
    quadB = float(quadEntry2.get())
    quadC = float(quadEntry3.get())

    for i in range(-17, 17):
        x1 = i
        x2 = x1 + 1
        y1 = (quadA * x1 ** 2) + (quadB * x1) + quadC
        y2 = (quadA * x2 ** 2) + (quadB * x2) + quadC
        canvas.create_line(x1, y1, x2, y2, width=3, fill="black")


def curve():
    linearInfo()
    quadraticInfo()
    pickLable = Label(root, text="Pick wether you want a line or a curve: ")
    pickLable.place(x=5, y=5)

    linearButton = Button(root, text="linear equation", command=lambda: linearInput())
    linearButton.place(x=10, y=50)

    quadraticButton = Button(
        root, text="quadratic equation", command=lambda: quadraticInput()
    )
    quadraticButton.place(x=10, y=100)

    resetButton = Button(root, text="reset", command=lambda: reset())
    resetButton.place(x=10, y=150)


from tkinter import *

root = Tk()
root.title("Curve Calculator")

canvas = Canvas(width=1000, height=800, bg="lightblue")
canvas.pack(expand=YES, fill=BOTH)

canvas.create_line(400, 100, 400, 500, width=4, fill="green")
canvas.create_line(650, 300, 150, 300, width=4, fill="green")

canvas.create_text(400, 90, text="y", fill="green")
canvas.create_text(660, 300, text="x", fill="green")

##pickLable = Label(root, text ="Pick wether you want a line or a curve: ")
##pickLable.place(x = 5, y = 5)
##
##linearButton = Button(root, text = 'linear equation', command = lambda: linearInput())
##linearButton.place(x = 10, y = 50)
##
##quadraticButton = Button(root, text = 'quadratic equation', command = lambda: quadraticInput())
##quadraticButton.place(x = 10, y = 100)
##
##resetButton = Button(root, text = 'reset', command = lambda: reset())
##resetButton.place( x = 10, y = 150)

curve()

mainloop()
