#!/usr/bin/python3

# SPDX-FileCopyrightText: © 2025 Spencer Rak
# SPDX-License-Identifier: MIT

# Exercise 5: Can You Change That To Numbers
# Write a program that has a function named numbers that:
# 
# Takes a string argument
# Returns a list of the ordinal numbers for each charater of the string

import argparse

def numbers(s: str) -> list[int]:
    """Return list of ordinal numbers for string chars
    """
    return [ord(x) for x in s]

def run(args):
    print(numbers(args.s))

def main():
    """This program returns a list of floats
    """
    ap = argparse.ArgumentParser()
    ap.add_argument("s", type=str, help="A string")
    args = ap.parse_args()

    run(args)

if __name__ == "__main__":
    main()
