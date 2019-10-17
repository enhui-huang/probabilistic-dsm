import pytest
import numpy as np
from p_dsm.p_tsm import ProbabilisticTsm2D

points = np.array([[1, 2], [3, 0], [5, 6]])
labels = np.array([1, 1, 1])
cone_points = np.array([[3, 10], [6, 6]])
cone_labels = np.array([-1, -1])


@pytest.fixture
def ptsm():
    ptsm = ProbabilisticTsm2D(2)
    return ptsm


def test_update_convex_hull(ptsm):
    for i in range(len(points)):
        ptsm.update_convex_hull(points[i], labels[i])
    assert ptsm.hull.pairs == {tuple([1, 2]): 1, tuple([3, 0]): 1, tuple([5, 6]): 1}
    assert ptsm.hull.count == {tuple([1, 2]): 1, tuple([3, 0]): 1, tuple([5, 6]): 1}
    assert ptsm.cones is None


def test_update_cones(ptsm):
    for i in range(len(cone_points)):
        ptsm.update_cones(cone_points[i], cone_labels[i])
    # TODO: find out how to compare two lists and array are identical later
    print(ptsm.init_cones)
    print(ptsm.init_cones_labels)
    assert ptsm.cones is None
    assert ptsm.hull is None


def test_update_both(ptsm):
    ptsm.update_convex_hull(points[0], labels[0])
    ptsm.update_cones(cone_points[0], cone_labels[0])
    ptsm.update_convex_hull(points[1], labels[1])
    assert ptsm.hull.pairs == {tuple([1, 2]): 1, tuple([3, 0]): 1}
    assert ptsm.hull.count == {tuple([1, 2]): 1, tuple([3, 0]): 1}
    assert ptsm.cones.cone_pairs == {tuple([3, 10]): -1}
    assert ptsm.cones.cone_count == {tuple([3, 10]): 1}


def test_is_inside_hull_yes(ptsm):
    ptsm.update_convex_hull(points[0], labels[0])
    ptsm.update_cones(cone_points[0], cone_labels[0])
    ptsm.update_convex_hull(points[1], labels[1])
    assert ptsm.is_inside_hull(np.array([2, 1])) == 1


def test_is_inside_hull_no(ptsm):
    ptsm.update_convex_hull(points[0], labels[0])
    ptsm.update_cones(cone_points[0], cone_labels[0])
    ptsm.update_convex_hull(points[1], labels[1])
    assert ptsm.is_inside_hull(np.array([0, 0])) == 0


def test_is_inside_cones_no(ptsm):
    ptsm.update_convex_hull(points[0], labels[0])
    ptsm.update_cones(cone_points[0], cone_labels[0])
    ptsm.update_convex_hull(points[1], labels[1])
    assert ptsm.is_inside_cones(np.array([4, 15])) == -1


def test_is_inside_cones_no(ptsm):
    ptsm.update_convex_hull(points[0], labels[0])
    ptsm.update_cones(cone_points[0], cone_labels[0])
    ptsm.update_convex_hull(points[1], labels[1])
    assert ptsm.is_inside_cones(np.array([5, 6])) == 0











