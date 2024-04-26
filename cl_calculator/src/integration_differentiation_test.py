import pytest
import integration_differentiation


def test_differentiation():
    formula = "3x^2 + 4x + 2"
    tokens = integration_differentiation.get_tokens(formula)
    constants, powers = integration_differentiation.get_constant_power(tokens)

    assert integration_differentiation.differentiation(constants, powers) == (
        [
            6.0,
            4.0,
            0.0,
        ],
        [1.0, 0.0, -1.0],
    )
    assert integration_differentiation.differentiation([1, -16], [4, 2]) == (
        [4, -32],
        [3, 1],
    )


def test_integration():
    formula = "3x^2 + 4x + 2"
    tokens = integration_differentiation.get_tokens(formula)
    constants, powers = integration_differentiation.get_constant_power(tokens)

    assert integration_differentiation.integration([2, -1], [2, 0]) == (
        [2 / 3, -1],
        [3, 1],
    )

    assert integration_differentiation.integration(constants, powers) == (
        [
            1.0,
            2.0,
            2.0,
        ],
        [
            3.0,
            2.0,
            1.0,
        ],
    )
