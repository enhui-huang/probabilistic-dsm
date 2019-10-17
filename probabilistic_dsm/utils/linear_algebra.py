import numpy as np
import copy


def get_orientation(o, a, b):
    """
    Given three 2D points o, a and b, by using the cross product of oa and ob
    :return: positive if o->a->b is in counter-clockwise order; negative if o->a->b is in clockwise order; zero if
    the three points are colinear
    """
    return (a[0] - o[0]) * (b[1] - a[1]) - (a[1] - o[1]) * (b[0] - a[0])


def is_between(o, a, b):
    """
    When o, a, b are colinear, further verify whether b is on the line segment oa
    :return: True if b on the line segment oa, False otherwise
    """
    o = convert_to_array(o)
    a = convert_to_array(a)
    b = convert_to_array(b)

    a_norm = np.linalg.norm(a - o)
    b_norm = np.linalg.norm(b - o)
    dot_product = np.dot(a-o, b-o)
    return True if (a_norm > b_norm and dot_product > 0) else False


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


def convert_to_array(arg):
    return arg if isinstance(arg, np.ndarray) else np.asarray(arg)



