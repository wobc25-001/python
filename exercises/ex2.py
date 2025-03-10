#!/usr/bin/python3

# SPDX-FileCopyrightText: © 2025 Spencer Rak
# SPDX-License-Identifier: MIT

# Exercise 2: Attention to Detail
# Create a program that takes (at least) three command line arguments. The first two
# will be integers and the third will be a float.
# 
# On one line, separated by spaces, print the sum of the first two arguments, the
# product of the first and third arguments, the first argument modulo the second,
# and the integer quotient of the first by the third.
# Add 1 to all three arguments.
# On a new line, print the first argument bitwise left shift 3, the second
# argument divided by 2 (not integer division), and the bitwise OR (operator) of
# the first and second arguments. (all separated by spaces.)
# On the last line, print the sum of the first argument (after the addition) and the
# total number of arguments, excluding the program name.
# Make sure the output numbers that are floats are at two digits of precision.


import argparse

def run(args):
    print(f"{args.a + args.b} {args.a * args.f} {args.a % args.b} {int(args.a // args.f)}")
    a, b, f = map(lambda x: x+1, (args.a, args.b, args.f))
    print(f"{a << 3} {b / 2} {a | b}")
    print(f"{a + 3}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("a", type=int, help="The first integer")
    ap.add_argument("b", type=int, help="The second integer")
    ap.add_argument("f", type=float, help="A float")
    args = ap.parse_args()

    run(args)

if __name__ == "__main__":
    main()
