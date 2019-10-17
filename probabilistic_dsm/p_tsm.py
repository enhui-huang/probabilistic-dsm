import numpy as np
from utils.object_operation import add_pair
from pConvexHull_2d import ProbabilisticConvexHull2D
from pConvexCones_2d import ProbabilisticConvexCones2D


class ProbabilisticTsm2D:
    """
    This method builds a tsm model containing a convex hull and convex cones from scratch
    """

    def __init__(self, dim):
        self.dim = dim
        self.hull = None
        self.cones = None
        self.hull_initialized = False
        self.cones_initialized = False
        self.init_hull = []
        self.init_cones = []
        self.init_hull_labels = []
        self.init_cones_labels = []

    def update_convex_hull(self, point, label):
        # TODO: remove these initial variables after the convex hull and convex cones have been created
        if not self.hull_initialized:
            self.init_hull.append(point)
            self.init_hull_labels.append(label)
            if len(self.init_hull) == self.dim:
                self.hull = ProbabilisticConvexHull2D(np.asarray(self.init_hull), np.asarray(self.init_hull_labels))
                self.hull_initialized = True
                if len(self.init_cones) > 0:
                    self.cones = ProbabilisticConvexCones2D(self.hull, np.asarray(self.init_cones),
                                                            np.asarray(self.init_cones_labels))
                    self.cones_initialized = True
        else:
            self.hull.add_vertex(point, label)

    def update_cones(self, point, label):
        # TODO: remove these initial variables after the convex hull and convex cones have been created
        if not self.cones_initialized:
            self.init_cones.append(point)
            self.init_cones_labels.append(label)
            if len(self.init_hull) >= self.dim:
                self.cones = ProbabilisticConvexCones2D(self.hull, np.asarray(self.init_cones),
                                                            np.asarray(self.init_cones_labels))
                self.cones_initialized = True
        else:
            self.cones.add_vertex(point, label)

    def is_inside_hull(self, point):
        return self.hull.is_inside(point) if (self.hull is not None) else 0

    def is_inside_cones(self, point):
        return self.cones.is_inside(point) if (self.cones is not None) else 0

    def is_uncertain(self):
        # TODO: think about how to define the uncertainty in this probabilistic model
        pass

    def get_uncertain_points(self):
        pass

    def get_three_set_metric(self):
        # TODO: think about how to calculate the three-set metric
        pass

    def get_hull(self):
        return self.hull

    def get_cones(self):
        return self.cones

