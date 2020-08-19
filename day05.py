#!/usr/bin/env python
# -*- coding: utf-8 -*-
# day05.py
"""
Advent of code day 5

Copyright (c) 2020, David Hoffman
"""


def add(x, y):
    return x + y


def prod(x, y):
    return x * y


def op3():
    pass


OPCODE = {1: add, 2: prod, 99: None}


def parse(instruction):
    """Parse a given instruction into OPCODE and three parameter modes"""
    instruction = f"{instruction:05d}"
    mode3, mode2, mode1 = map(int, instruction[:3])
    opcode = int(instruction[3:])
    return mode1, mode2, mode3, opcode
