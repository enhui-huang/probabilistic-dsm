import utils.linear_algebra as la
import numpy as np


def test_get_orientation_coliner():
    o = [1, 4]
    a = [2, 5]
    b = [3, 6]
    assert la.get_orientation(o, a, b) == 0


def test_get_orientation_counter_clockwise():
    o = [1, 4]
    a = [2, 3]
    b = [3, 6]
    assert la.get_orientation(o, a, b) > 0


def test_get_orientation_clockwise():
    o = [1, 4]
    a = [2, 6]
    b = [3, 6]
    assert la.get_orientation(o, a, b) < 0


def test_is_between_yes():
    o = [1, 4]
    a = [2, 5]
    b = [3, 6]
    assert la.is_between(o, a, b) == True


def test_is_between_no():
    o = [1, 4]
    a = [2, 5]
    b = [3, 6]
    assert la.is_between(o, b, a) == False


def test_is_inside_yes():
    pairs = {tuple([1, 4]): 1, tuple([2, 0]): 1, tuple([3, 6]): 1}
    test_point = np.array([2, 4])
    assert la.is_inside(pairs, test_point) == 1


def test_is_inside_yes_on_boundary():
    pairs = {tuple([1, 4]): 1, tuple([2, 0]): 1, tuple([3, 6]): 1}
    test_point = np.array([2, 5])
    assert la.is_inside(pairs, test_point) == 1


def test_is_inside_no():
    pairs = {tuple([1, 4]): 1, tuple([2, 0]): 1, tuple([3, 6]): 1}
    test_point = np.array([2, -1])
    assert la.is_inside(pairs, test_point) == 0


