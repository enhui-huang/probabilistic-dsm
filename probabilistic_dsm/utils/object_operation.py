import numpy as np


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


def add_pair(pairs, count, point, label):
    current_point = ()
    if not isinstance(point, tuple):
        current_point = tuple(point)
    if current_point in pairs.keys():
        current_label = pairs.get(current_point)
        current_count = count.get(current_point)
        pairs[current_point] = (current_label * current_count + label) / (current_count + 1)
        count[current_point] += 1
    else:
        pairs[current_point] = label
        count[current_point] = 1

