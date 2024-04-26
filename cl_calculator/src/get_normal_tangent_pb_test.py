import pytest
import get_normal_tangent_pb


def test_get_highest_power():
    formula = "5x^3 + 4x^2 - 4x - 4"
    tokens = get_normal_tangent_pb.get_tokens(formula)
    constants, powers = get_normal_tangent_pb.get_constant_power(tokens)

    assert get_normal_tangent_pb.get_highest_power(powers) == 3.0


def test_line_yintercept():
    m = 2
    x = 3
    y = 5

    assert get_normal_tangent_pb.line_yintercept(m, x, y) == -1


def test_get_tangent():
    formula = "5x^3 + 4x^2 - 4x - 4"
    tokens = get_normal_tangent_pb.get_tokens(formula)
    constants, powers = get_normal_tangent_pb.get_constant_power(tokens)
    x = 1
    y = 1

    assert get_normal_tangent_pb.get_tangent(powers, constants, x, y) == (
        19,
        [19, -18],
        [1, 0],
    )


def test_get_normal():
    formula = "2x + 6"
    tokens = get_normal_tangent_pb.get_tokens(formula)
    constants, powers = get_normal_tangent_pb.get_constant_power(tokens)
    x = 2
    y = 3

    assert get_normal_tangent_pb.get_normal(powers, constants, x, y) == (
        [-0.5, 4.0],
        [
            1.0,
            0.0,
        ],
    )


def test_get_pb():
    formula = "2x + 6"
    tokens = get_normal_tangent_pb.get_tokens(formula)
    constants, powers = get_normal_tangent_pb.get_constant_power(tokens)
    startx = -2
    starty = 2
    endx = 2
    endy = 10

    assert get_normal_tangent_pb.get_pb(
        powers, constants, startx, starty, endx, endy
    ) == ([-0.5, 6.0], [1.0, 0.0])
