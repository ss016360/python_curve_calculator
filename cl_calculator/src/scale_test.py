import pytest
import scale


def test_get_fixed_scale_values():
    assert scale.get_fixed_scale_values(-4, 4, 100, 900) == (100, 500)


def test_get_y_scale():
    assert scale.get_y_scale(3, -5, 5, 600, 100) == 500


def test_get_x_scale():
    assert scale.get_x_scale(3, -5, 5, 100, 600) == 500
