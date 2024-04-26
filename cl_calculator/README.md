# CL Calculator

## Current Problem
- I cannot create x and y text next to the graph
## NEXT
- See if I can highlight something that already exists when I try to save it
- Add a save button to the equation screen and add the results to that equation
- Make the equation that is entered in the save screen appear, and remove the text box from the equation screen
- See if I can display the coordinates of where the user clicks on the graph
- Organise my equation screen
### This Week


### Next Week


## Contributing to the project
Prep steps:
1. install Tkinter globally

Steps:
1. download repo & change directory to project
2. create a new branch
3. create & activate virtual environment; install modules
4. implement changes
5. add, commit, push, create a pull request, merge

```sh
# ------- PREP STEPS ------- #
#1. install Tkinter globally
brew install python-tk

# -------   STEPS    ------- #
#1. download repo & change directory to project
git clone git@github.com:molcathy/cl_calculator.git
cd cl_calculator

#2. create branch
git checkout -b <myBranch>

#3. create & activate virtual environment; install module
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

#4. implement changes

#5. TEST
pytest -v src/

#6. add, commit, push, create a pull request, merge
```

## Project Goals
1.	The user can enter the equation (or a polynomial) as a string and the program will translate and slice elements of that string, putting it together into a format that the computer understands. []
2.	On the interface/screen of the program you can have buttons that make it easier to navigate through the program, such as:
    1.	Clearing the screen []
    2.	Home button, allows you to go to the default screen which is the screen where the equation is entered []
    3.	Display Button, to display the equation that is written []
    4.	Storage button, that allows you to bring and use in the calculator []
    5.	Formula buttons to apply to the equation given (integration, differentiation, y intersection points etc.) []
    6.	The number of graphs to hold and display []
    7.	Picking a point to show the coordinates of []
    8.	Saving a graph []
3.	To apply formulas on the equation that the computer understands such as:
    1.	Integration [x]
    2.	Differentiation [x]
    3.	Area underneath a graph [x]
    4.	Displaying a point on the graph [] not sure about this
    5.	Figuring out the tangent [x]
    6.	Figuring out the normal [x]
    7.	Figuring out the perpendicular bisector [x]
    8.	Figuring out the minimum and maximum (or there might be a minimum turning point and a maximum turning point depending on the graph) [x]
    9.	Figuring out the asymptote []
    10.	Where graphs intersect []
    11.	Where the y-intersect is [x]
    12.	Where the x-intersect is [x]
    13.	Doing a graph to any power [x]
    14.	Drawing a graph with a positive or negative gradient [x]
    15.	Scaling the graph to fit the space given []
    16.	Only allowing the values to be drawn that are inside the graph [x]
4.	To clear the screen []
5.	To have a screen where you can save and upload polynomials and equations of a line so that the user can pull it up and use it again. []
6.	To be able to hold up to 5 lines or curves []
7.	To have a simple and easy design that makes it easy for the user to navigate within the program:
    1.	buttons at the top of the screen []
    2.	always being able to go back to the home screen regardless of where you are []
    3.	clear navigation buttons, []
    4.	clear: delete, reset and save buttons []
    5.	have the buttons large enough []
    6.	have the buttons evenly spaced out enough []
    7.	make sure for the display the graph is properly scaled []
8.	Making sure the program can properly handle any errors of entering information:
    1.	Incorrect letters and symbols []
    2.	Entering nothing []
    3.	Entering things in the wrong format []
9.	Where you save the equations of a line to have a format where you can click to pick 1 to 5 from a list of saved files of equations of a line as a list, then to click a ‘use’ button which automatically directs you to the home page with all of the equations of the line displayed and you can now use. []
10.	When you have multiple equations of a line displayed:
    1.	You can see each equation displayed one beneath each other on the home page []
    2.	When you want to apply a formula to an equation of a line, you click on the equation of the line you want to apply it to and then the button 1f the formula you want to apply. []
    3.	For displaying you automatically highlight intersection points, you can also pick from the homepage which equations you want to display. []
