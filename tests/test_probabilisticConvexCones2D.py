import pytest
import numpy as np
from pConvexHull_2d import ProbabilisticConvexHull2D
from pConvexCones_2d import ProbabilisticConvexCones2D


@pytest.fixture
def cones():
    points = np.array([[1, 2], [3, 0], [5, 6]])
    labels = np.array([1, 1, 1])
    hull = ProbabilisticConvexHull2D(points, labels)
    cone_points = np.array([[3, 10], [6, 6]])
    cone_labels = np.array([-1, -1])
    return ProbabilisticConvexCones2D(hull, cone_points, cone_labels)


def test_add_vertex(cones):
    cones.add_vertex(np.array([3, 9]), -1)
    assert cones.cone_pairs == {tuple([3, 10]): -1, tuple([6, 6]): -1, tuple([3, 9]): -1}
    assert cones.cone_count == {tuple([3, 10]): 1, tuple([6, 6]): 1, tuple([3, 9]): 1}


def test_add_vertex_add_duplicates(cones):
    cones.add_vertex(np.array([3, 10]), -1)
    assert cones.cone_pairs == {tuple([3, 10]): -1, tuple([6, 6]): -1}
    assert cones.cone_count == {tuple([3, 10]): 2, tuple([6, 6]): 1}


def test_add_vertex_add_uncertain_duplicates(cones):
    cones.add_vertex(np.array([3, 10]), 0.2)
    assert cones.cone_pairs == {tuple([3, 10]): -0.4, tuple([6, 6]): -1}
    assert cones.cone_count == {tuple([3, 10]): 2, tuple([6, 6]): 1}


def test_is_inside_yes(cones):
    assert cones.is_inside(np.array([3, 12])) == -1


def test_is_inside_yes_on_boundary(cones):
    assert cones.is_inside(np.array([10, 6])) == -1


def test_is_inside_no_case1(cones):
    assert cones.is_inside(np.array([0, 0])) == 0


def test_is_inside_no_case2(cones):
    assert cones.is_inside(np.array([3, 9])) == 0
