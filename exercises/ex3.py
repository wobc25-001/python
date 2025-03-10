#!/usr/bin/python3

# SPDX-FileCopyrightText: © 2025 Spencer Rak
# SPDX-License-Identifier: MIT

# Exercise 3: Conditional Statements
# Create a program that takes (at least) three command line
# arguments. The first two will be integers and the third will be a string.
# 
# Prints the larger of the two integers. If they are equal, do not print
# either one.
# 
# If the word "time" appears in the string, print the sum of the
# integers.
# 
# If both the integers are odd, or one of them is a multiple of 3, print
# the string.
# If there are more than three command line arguments (excluding
# the filename), print the word "errorTM.

import argparse

def run(args):
    a, b, s = (args.a, args.b, args.s)
    if a != b:
        print(a if a > b else b)
    if "time" in s:
        print(a + b)
    if (
        (a % 2 == 1 and b % 2 == 1)
        or a % 3 == 0
        or b % 3 == 0
    ):
        print(s)


def main():
    """This program only accepts 3 arguments
    """
    ap = argparse.ArgumentParser()
    ap.add_argument("a", type=int, help="The first integer")
    ap.add_argument("b", type=int, help="The second integer")
    ap.add_argument("s", type=str, help="A string")
    args = ap.parse_args()

    run(args)

if __name__ == "__main__":
    main()
