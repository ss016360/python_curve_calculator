import pytest
import get_lines_intersect


def test_sorted_insert():
    p1 = [3, 1, 0]
    c1 = [2, 6, 5]
    p = 2
    assert get_lines_intersect.sorted_insert(p1, c1, p) == ([3, 2, 1, 0], [2, 0, 6, 5])


def test_merge_polynomials():
    p1 = [3, 2, 0]
    p2 = [2, 1, 0]
    c1 = [5, 6, 8]
    c2 = [4, 5, 2]
    assert get_lines_intersect.merge_polynomials(p1, c1, p2, c2) == (
        [3, 2, 1, 0],
        [
            5,
            2,
            -5,
            6,
        ],
    )


def test_get_intersect():
    x_start = -5
    x_end = 5
    y_start = -5
    y_end = 5
    p1 = [1, 0]
    p2 = [1, 0]
    c1 = [3, -3]
    c2 = [2.3, 4]

    assert get_lines_intersect.get_intersect(
        p1, c1, p2, c2, x_start, x_end, y_start, y_end
    ) == ([10], [27])
