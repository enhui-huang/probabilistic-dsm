"""
Created on Mon Oct 14 17:12:05 2019

@author: enhui
"""

import numpy as np
from utils.linear_algebra import is_inside
from utils.object_operation import get_point_label_pairs, add_pair


class ProbabilisticConvexHull2D:
    """Convex hulls are widely applied in many real wrold problems, including but not limited to computer
    graphics, pattern recognition, image processing, robotics and statistics. For some of these applications,       
    such as sensor databases, location-based services or computer vision, the location and sometimes even the 
    existence of data is uncertain. This probabilistic version of convex hulls is thus proposed to
    characterize the probability distribution of uncertain data.
    
    
    References
    ----------
    [1] Convex Hulls under Uncertainty.Pankaj Agarwal, Sariel Har-Peled, Subhash Suri, Hakan Yildiz and 
    Wuzhou Zhang. Algorithmica 79(2), 340-367, 2017.
    """

    def __init__(self, points, labels):
        assert (isinstance(points, np.ndarray)), "The input is not an array"
        assert (len(points) == len(labels)), "The size of points does not match the size of labels."
        assert (((labels >= 0) & (labels <= 1)).all()), "The value of a probabilistic label must between 0 and 1."

        if not isinstance(labels, np.ndarray):
            labels = np.asarray(labels)

        pairs, count = get_point_label_pairs(points, labels)
        self.pairs = pairs
        self.count = count

    def add_vertex(self, point, label):
        add_pair(self.pairs, self.count, point, label)

    def is_inside(self, test_point):
        return is_inside(self.pairs, test_point)








