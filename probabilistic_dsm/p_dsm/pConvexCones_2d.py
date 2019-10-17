import numpy as np
import copy
from p_dsm.pConvexHull_2d import ProbabilisticConvexHull2D
from utils.object_operation import get_point_label_pairs, add_pair


class ProbabilisticConvexCones2D:
    """
    This class constructs a convex cone in 2D space for each point that has opposite label to points in a convex hull P.
    Given a point n1 whose label is opposite to P, we can construct a convex cone Cone(n1) with n1 being the extreme
    point. For a incoming data point q and q has the same label as n1, it is located in the Cone(n1) if and only if
    n1 in hull(R and q).
    """

    def __init__(self, hull, extreme_points, labels):
        assert (isinstance(hull, ProbabilisticConvexHull2D)), "This is not a convex hull!"
        assert (isinstance(extreme_points, np.ndarray)), "The input is not an array"
        assert (len(extreme_points) == len(labels)), "The size of points does not match the size of labels."
        assert (((labels <= 0) & (labels >= -1)).all()), "The value of a probabilistic label must between -1 and 0."

        if not isinstance(labels, np.ndarray):
            labels = np.asarray(labels)

        cone_pairs, cone_count = get_point_label_pairs(extreme_points, labels)
        self.hull = hull
        self.cone_pairs = cone_pairs
        self.cone_count = cone_count

    def add_vertex(self, point, label):
        add_pair(self.cone_pairs, self.cone_count, point, label)

    def is_inside(self, test_point):
        res = 0
        new_hull = copy.deepcopy(self.hull)
        new_hull.add_vertex(test_point, 1)

        cone_pairs = self.cone_pairs
        for extreme_point in cone_pairs.keys():
            res += cone_pairs.get(extreme_point) * new_hull.is_inside(extreme_point)

        return max(res, -1)
