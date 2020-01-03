#!/usr/bin/env python
# -*- coding: utf-8 -*-
# day03.py
"""
Advent of code day 3

Copyright (c) 2019, David Hoffman

"""

import numpy as np

test_inoutputs = (
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
    coords = [(0, 0)]
    path = path[::-1]
    while path:
        step = path.pop()
        direction, length = step[0], int(step[1:])
        if direction in {"L", "U"}:
            length *= -1

        y, x = coords[-1]

        if direction in {"L", "R"}:
            coords


def main():
    print("test")


if __name__ == "__main__":
    main()
