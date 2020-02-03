#!/usr/bin/env python
# -*- coding: utf-8 -*-
# day03.py
"""
Advent of code day 3

Copyright (c) 2019, David Hoffman

"""


test_inoutputs = (
    (("R8,U5,L5,D3".split(","), "U7,R6,D4,L4".split(",")), 6),
    (
        (
            "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(","),
            "U62,R66,U55,R34,D71,R55,D58,R83".split(","),
        ),
        159,
    ),
    (
        (
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(","),
            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(","),
        ),
        135,
    ),
)


def convert_to_coords(path):
    """Convert text path into coordinate list"""
    coords = [(0, 0)]
    # reverse path so that pop removes first, then second, then third, etc.
    path = path[::-1]
    while path:
        # get next step
        step = path.pop()

        # retrieve direction and length
        direction, length = step[0], int(step[1:])
        if direction in {"L", "U"}:
            length *= -1

        # get last coordinates
        y, x = coords[-1]

        # make new coordinates
        if direction in {"L", "R"}:
            coords.append((y, x + length))
        else:
            coords.append((y + length, x))

    return coords


def direction(segment):
    (y0, x0), (y1, x1) = segment
    if y0 == y1:
        return "H"
    elif x0 == x1:
        return "V"
    else:
        raise RuntimeError


def test_cross(segment0, segment1):

    # segments are parallel, no way to cross
    dir0 = direction(segment0)
    dir1 = direction(segment1)
    if dir0 == dir1:
        return None

    (y00, x00), (y01, x01) = segment0
    (y10, x10), (y11, x11) = segment1

    # if the direction of segment 0 is vertical then
    # we can test whether the x location crosses the other
    # and whether the
    if dir0 == "V":
        assert x01 == x00
        if x00 <= max(x10, x11) and x00 >= min(x10, x11):
            # now we need to check y
            if y11 <= max(y00, y01) and y11 >= min(y00, y01):
                return y11, x00
    else:
        assert y01 == y00
        if y00 <= max(y10, y11) and y00 >= min(y10, y11):
            # now we need to check y
            if x11 <= max(x00, x01) and x11 >= min(x00, x01):
                return y00, x11

    return None


def find_intersections(coord0, coord1):
    intersections = []
    for i in range(len(coord0) - 1):
        segment0 = coord0[i : i + 2]
        for j in range(len(coord1) - 1):
            segment1 = coord1[j : j + 2]
            coord = test_cross(segment0, segment1)
            if coord:
                intersections.append(coord)
    return intersections


def calc_distance(intersections):
    return [sum(map(abs, coord)) for coord in intersections]


def get_min_dist(paths):
    coords = [convert_to_coords(path) for path in paths]
    intersections = find_intersections(*coords)
    distances = calc_distance(intersections)
    return min(distances[1:])


def test():
    for paths, distance in test_inoutputs:
        assert distance == get_min_dist(paths)


def main():
    # read in data
    with open("day03.txt", "r") as fp:
        txt = fp.read()

    paths = [path.split(",") for path in txt.strip().split("\n")]
    print(get_min_dist(paths))


if __name__ == "__main__":
    test()
    main()
