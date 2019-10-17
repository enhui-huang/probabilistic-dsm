import pytest
import numpy as np
from p_dsm.pConvexHull_2d import ProbabilisticConvexHull2D


@pytest.fixture
def hull():
    points = np.array([[1, 2], [3, 0], [5, 6]])
    labels = np.array([1, 1, 1])
    return ProbabilisticConvexHull2D(points, labels)


def test_add_vertex(hull):
    hull.add_vertex(np.array([3, 9]), 1)
    assert hull.pairs == {tuple([1, 2]): 1, tuple([3, 0]): 1, tuple([5, 6]): 1, tuple([3, 9]): 1}
    assert hull.count == {tuple([1, 2]): 1, tuple([3, 0]): 1, tuple([5, 6]): 1, tuple([3, 9]): 1}


def test_add_vertex_add_duplicates(hull):
    hull.add_vertex(np.array([3, 0]), 1)
    assert hull.pairs == {tuple([1, 2]): 1, tuple([3, 0]): 1, tuple([5, 6]): 1}
    assert hull.count == {tuple([1, 2]): 1, tuple([3, 0]): 2, tuple([5, 6]): 1}


def test_add_vertex_add_uncertain_duplicates(hull):
    hull.add_vertex(np.array([3, 0]), 0.2)
    assert hull.pairs == {tuple([1, 2]): 1, tuple([3, 0]): 0.6 , tuple([5, 6]): 1}
    assert hull.count == {tuple([1, 2]): 1, tuple([3, 0]): 2, tuple([5, 6]): 1}
