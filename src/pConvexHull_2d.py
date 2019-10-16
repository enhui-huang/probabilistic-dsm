#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 17:12:05 2019

@author: enhui
"""

import numpy as np
import copy


def get_point_label_pairs(points, labels):
    assert (len(points) == len(labels)), "The inputs have inconsistent size!"
    size = len(labels)
    points = list(map(tuple, points))
    pairs, count = {}, {}
    for i in range(size):
        point = points[i]
        if len(pairs) > 0 and (point in pairs.keys()):
            pairs[point] += labels[i]
            count[point] += 1
        else:
            pairs[point] = labels[i]
            count[point] = 1

    # average the probabilities of duplicated points
    for key in count.keys():
        if count[key] > 1:
            pairs[key] /= count[key]

    return pairs, count


def get_orientation(o, a, b):
    """
    Given three 2D points o, a and b, by using the cross product of oa and ob
    :return: positive if o->a->b is in counter-clockwise order; negative if o->a->b is in clockwise order; zero if
    the three points are colinear
    """
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def is_between(o, a, b):
    """
    When o, a, b are colinear, further verify whether b is on the line segment oa
    :return: True if b on the line segment oa, False otherwise
    """
    dot_product = np.linalg.norm(a - o)
    segment_length = np.linalg.norm(b - o)
    return True if 0 < dot_product < segment_length else False


def is_inside(pairs, test_point):
    """
    :return: probability of a point inside the convex hull
    """
    points = pairs.keys()
    p_empty, p_witness = 1, 0

    # if a point coincides with a vertex v in the convex hull, the probability of this point being in the convex
    # hull is defined: P(v exists) + P(v does not exist) * is_inside(hull\v)
    if tuple(test_point) in points:
        duplicate = tuple(test_point)
        new_points = copy.deepcopy(points)
        del new_points[duplicate]
        return points[duplicate] + (1 - points[duplicate]) * is_inside(new_points, test_point)
    for wp in points:
        p_empty *= (1 - pairs.get(wp))
        p_right = 1
        right_points = []
        for ap in points:
            if wp != ap:
                orientation = get_orientation(test_point, wp, ap)
                # testpoint might be colinear with two or more other points
                if orientation < 0 or (orientation == 0 and not is_between(test_point, wp, ap)):
                    right_points.append(ap)
        if len(right_points) > 0:
            for point in right_points:
                p_right *= (1 - pairs.get(point))
        p_witness += pairs.get(wp) * p_right

    return 1 - (p_empty + p_witness)


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
        if not isinstance(labels, np.ndarray):
            labels = np.asarray(labels)
        assert (np.all(0 <= labels <= 1)), "The value of a probabilistic label must between 0 and 1."
        pairs, count = get_point_label_pairs(points, labels)
        self.pairs = pairs
        self.count = count

    def add_vertex(self, point, label):
        current_point = ()
        if not isinstance(point, tuple):
            current_point = tuple(point)
        if current_point in self.pairs.keys():
            current_label = self.pairs.get(current_point)
            current_count = self.count.get(current_point)
            self.pairs[current_point] = (current_label * current_count + label) / (current_count + 1)
            self.count[current_point] += 1
        else:
            self.pairs[current_point] = label
            self.count[current_point] = 1

    def is_inside(self, test_point):
        return is_inside(self.pairs, test_point)








