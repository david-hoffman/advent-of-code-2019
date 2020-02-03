#!/usr/bin/env python
# -*- coding: utf-8 -*-
# day04.py
"""
Advent of code day 4

Copyright (c) 2020, David Hoffman
"""


test_inputs = ((111111, True), (223450, False), (123789, False))


def double(key):
    """check if there are doubles"""
    key = str(key)
    for k0, k1 in zip(key[:-1], key[1:]):
        if k0 == k1:
            return True
    return False


def monotonic(key):
    """Check if monotonic"""
    # convert to list of digits
    key = [int(k) for k in str(key)]
    for k0, k1 in zip(key[:-1], key[1:]):
        if k0 > k1:
            return False
    return True


def double2(key):
    """check if there are any doubles that are isolated"""
    # make a list of the key in the right order
    key = list(str(key))[::-1]
    length = 1
    k0 = key.pop()
    # cycle through keys
    while key:
        k1 = key.pop()
        if k0 == k1:
            length += 1
        else:
            if length == 2:
                return True
            length = 1
        k0 = k1
    if length == 2:
        return True
    return False


def test():
    for key, truth in test_inputs:
        assert double(key) and monotonic(key) == truth


def main():
    valid_keys = filter(double, range(372037, 905157 + 1))
    valid_keys = tuple(filter(monotonic, valid_keys))
    print("Answer 1:", len(valid_keys))
    print("Answer 2:", len(tuple(filter(double2, valid_keys))))


if __name__ == "__main__":
    main()
