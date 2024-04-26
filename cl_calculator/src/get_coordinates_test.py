import pytest
import get_coordinates


def test_get_coordinates():
    formula = "3x^2 + 4x + 2"
    coordinates_x, coordinates_y = get_coordinates.get_coordinates(
        -5, 5, 0, 100, formula
    )
    coordinates_x = [round(coordinate, 3) for coordinate in coordinates_x]
    coordinates_y = [round(coordinate, 3) for coordinate in coordinates_y]

    coordinates_x.sort()
    coordinates_y.sort()

    """
    The limits set for x: -5, 5
    The limits set for y: 0, 100
    """
    assert (
        coordinates_x[0] >= -5
        and coordinates_x[-1] <= 5
        and coordinates_y[0] >= 0.667  # above 0
        and coordinates_y[-1] <= 97  # below 100
    )
    """
    limits, so a mathematical formula so when you enter the limits of x: -5 and 5,
    you figure out the y limits within that range, which is 97 and 0.667(found by getting the turning point),
    so you can figure out the ammount of x coordinates to be generated in the range of -5 and 5

    x coordinates determine the y limits so that you can get all the x coordinates from -5 to 5
    """
    assert len(coordinates_x) == (
        (abs(-5 - 5) / 0.01) + 1
    )  # you add 1 to count the first coordinate as well
