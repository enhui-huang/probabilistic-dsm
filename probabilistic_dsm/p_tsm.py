from pConvexHull_2d import ProbabilisticConvexHull2D
from pConvexCones_2d import ProbabilisticConvexCones2D


class ProbabilisticTsm2D:
    """
    This method builds a tsm model containing a convex hull and convex cones from scratch
    """

    def __init__(self, dim):
        self.dim = dim
        self.convex_hull = None
        self.convex_cones = None
        self.hull_initialized = False
        self.cones_initialized = False
        self.init_hull_points = []
        self.init_cones_points = []

    def update_convex_hull(self, point, label):
        pass
        # if not self.hull_initialized:
        #     self.init_hull_points.append(point)
        #     if len(self.init_hull_points) == self.dim and len(self.init_cones_points) > 0:
        #          for cone_point in self.init_cones_points
        #
