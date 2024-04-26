"""
research:
python save text file to selected folder

tkinter folder widget
"""

import json

"""
formulas.json
--------------------------------
[
    {
        "name": "Formula for Q2",
        "formula": "2x + 3",
        "results": {
            "x_intercept": "-5"
        }
    },
    {
        "name": "Formula for Q3",
        "formula": "5x^2"
    }
]
"""

formulas = []
# results is a dictionary
def format_data(data_list, list_dictionary):
    if len(data_list) == 2:
        name = data_list[0]
        formula = data_list[1]
        list_dictionary.append(
            {"name": str(name), "formula": str(formula), "results": {}}
        )


# for Loading the data from the text file to the program and savaing the data
# back onto the file, rewriting the whole file
def load_data(file_path):
    data = []
    with open(file_path) as f:
        jsonData = f.read()
        data = json.loads(jsonData)
    return data


# load_data("formulas.json")  # Return [], [{"name": "..", "formula": "..."}]


def save_data(file_path, data):
    # Saving
    with open(file_path, "w") as f:
        jsonData = json.dumps(data)
        f.write(jsonData)


# data.append({"name": "Whatever the user entered", "formula": "5x + 3"})


def remove_formula_by_name(data, name):
    new_data = []
    for formula in data:
        if formula["name"] != name:
            new_data.append(formula)
    return new_data


def search_dictionary(name, list_dictionary):
    for i in range(len(list_dictionary)):
        if list_dictionary[i]["name"] == name:
            return i

    return -1


def main():
    pass


if __name__ == "__main__":
    main()
