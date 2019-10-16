import numpy as np
import utils.object_operation as ot


def test_get_point_label_pairs():
    points = np.array([[1, 2], [3, 4], [5, 6]])
    labels = np.array([1, 0.1, 0.5])
    pairs, count = ot.get_point_label_pairs(points, labels)
    assert pairs == {tuple([1, 2]): 1, tuple([3, 4]): 0.1, tuple([5, 6]): 0.5}
    assert count == {tuple([1, 2]): 1, tuple([3, 4]): 1, tuple([5, 6]): 1}
