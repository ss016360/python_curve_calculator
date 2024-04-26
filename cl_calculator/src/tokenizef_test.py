import pytest
import tokenizef


def test_get_tokens():
    assert tokenizef.get_tokens("5x^3 + 4x^2 - 4x - 4") == [
        "+5x^3",
        "+4x^2",
        "-4x",
        "-4",
    ]


def test_get_tokens_start_with_plus():
    assert tokenizef.get_tokens("+ 5x^3 + 4x^2 - 4x - 4") == [
        "+5x^3",
        "+4x^2",
        "-4x",
        "-4",
    ]


def test_get_tokens_start_with_plus_no_space():
    assert tokenizef.get_tokens("+5x^3 + 4x^2 - 4x - 4") == [
        "+5x^3",
        "+4x^2",
        "-4x",
        "-4",
    ]


def test_get_tokens_start_with_minus():
    assert tokenizef.get_tokens("- 5x^3 + 4x^2 - 4x - 4") == [
        "-5x^3",
        "+4x^2",
        "-4x",
        "-4",
    ]


def test_get_tokens_start_with_minus_no_space():
    assert tokenizef.get_tokens("-5x^3 + 4x^2 - 4x - 4") == [
        "-5x^3",
        "+4x^2",
        "-4x",
        "-4",
    ]


def test_get_tokens_no_spaces():
    assert tokenizef.get_tokens("5x^3 +4x^2 -4x -4") == ["+5x^3", "+4x^2", "-4x", "-4"]


def test_string_constant_power():
    assert tokenizef.string_constant_power([3, 4, -2], [2, 1, 0]) == ("3x^2 + 4x - 2")


def test_generate_equation():
    constants = [2, 4]
    powers = [1, 0]

    fx = tokenizef.generate_equation(constants, powers)
    y = fx(0)
    y_2 = fx(-2)

    assert y == 4
    assert y_2 == 0
