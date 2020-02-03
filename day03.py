#!/usr/bin/env python
# -*- coding: utf-8 -*-
# day03.py
"""
Advent of code day 3

Copyright (c) 2019, David Hoffman

"""


test_inoutputs = (
    (("R8,U5,L5,D3".split(","), "U7,R6,D4,L4".split(",")), 6, 30),
    (
        (
            "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(","),
            "U62,R66,U55,R34,D71,R55,D58,R83".split(","),
        ),
        159,
        610,
    ),
    (
        (
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(","),
            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(","),
        ),
        135,
        410,
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


def test_cross(segment0, segment1):
    """Test if segments cross and return the location of where
    segment1 crosses segment0 (this distinction is important for
    parallel segments"""

    (y00, x00), (y01, x01) = segment0
    (y10, x10), (y11, x11) = segment1

    # if the direction of segment 0 is vertical
    if x01 == x00:
        # check whether they cross in the horizontal direction
        if x00 <= max(x10, x11) and x00 >= min(x10, x11):
            # Where do they cross in y
            if y11 <= max(y00, y01) and y11 >= min(y00, y01):
                return y11, x00
            if y10 <= max(y00, y01) and y10 >= min(y00, y01):
                return y10, x00
    else:
        # no diagonal segments
        assert y01 == y00, "Failed, diagonal segment"
        # same as above but for a horizontal segment 1
        if y00 <= max(y10, y11) and y00 >= min(y10, y11):
            if x11 <= max(x00, x01) and x11 >= min(x00, x01):
                return y00, x11
            if x10 <= max(x00, x01) and x10 >= min(x00, x01):
                return y00, x10

    return None


def find_intersections(coord0, coord1):
    """Find all the intersections between two paths, assuming
    they've been converted to coordinates"""
    intersections = []
    for i in range(len(coord0) - 1):
        segment0 = coord0[i : i + 2]
        for j in range(len(coord1) - 1):
            segment1 = coord1[j : j + 2]
            coord = test_cross(segment0, segment1)
            if coord:
                # we want to keep track of where the cross is, for later
                # alternatively we could have kept track of the length
                # but because of the question this is how it was written
                intersections.append((coord, i, j))
    return intersections


def calc_distance(intersections):
    """calculate the Manhattan distances for all intersections"""
    return [sum(map(abs, coord)) for coord, _, _ in intersections]


def calc_steps(coords):
    """calculate the number of steps in a path"""
    steps = 0
    for i in range(len(coords) - 1):
        segment = coords[i : i + 2]
        (y0, x0), (y1, x1) = segment
        steps += abs(y0 - y1) + abs(x0 - x1)
    return steps


def get_min_dist(paths):
    """Return the distance to the closest intersection"""
    coords = [convert_to_coords(path) for path in paths]
    intersections = find_intersections(*coords)
    distances = calc_distance(intersections[1:])
    return min(distances)


def get_min_steps(paths):
    """Get the minimum number of steps to get to the intersection"""
    coords = [convert_to_coords(path) for path in paths]
    intersections = find_intersections(*coords)
    step_collection = []
    for coord, i, j in intersections[1:]:
        new_coords0 = coords[0][:i] + [coord]
        new_coords1 = coords[1][:j] + [coord]
        step_collection.append(calc_steps(new_coords0) + calc_steps(new_coords1))

    return min(step_collection)


def test():
    """Run test cases"""
    for paths, distance, steps in test_inoutputs:
        # first part
        assert distance == get_min_dist(paths), get_min_dist(paths)
        # second part
        assert steps == get_min_steps(paths), get_min_steps(paths)


def main():
    # read in data
    with open("day03.txt", "r") as fp:
        txt = fp.read()

    paths = [path.split(",") for path in txt.strip().split("\n")]
    print("Answer 1:", get_min_dist(paths))
    print("Ansert 2:", get_min_steps(paths))


if __name__ == "__main__":
    test()
    main()
