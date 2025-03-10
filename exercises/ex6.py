#!/usr/bin/python3

# SPDX-FileCopyrightText: © 2025 Spencer Rak
# SPDX-License-Identifier: MIT

# Exercise 6: Loops
# Create a program that takes one integer command line argument.
# 
# Ensure the argument is an integer, if not the program doesn't do
# anything.
# 
# For each number between 1 and the argument (inclusive), print the
# word "triangle" if the number is a multiple of three.
# Print "square" if it is a multiple of four.
# If it is @ multiple of 12, do not print triangle or square. Instead, print
# "x dozen" where x is the numeral representing how many dozen
# 
# you're at("1 dozen" for 12, "2 dozen" for 24, etc.)
# Lastly, print the sum of the numbers between 1 and the argument
# (inclusive).

import argparse


def run(args):
    for i in range(1, args.i+1):
        match i:
            # broken
            case _ if i % 12 == 0:
                print(f"{i / 12} dozen")
                break
            case _ if i % 3 == 0:
                print("triangle")
                break
            case _ if i % 4 == 0:
                print("square")
                break

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("i", type=int, help="An integer")
    args = ap.parse_args()

    run(args)

if __name__ == "__main__":
    main()
