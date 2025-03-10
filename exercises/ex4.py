#!/usr/bin/python3

# SPDX-FileCopyrightText: © 2025 Spencer Rak
# SPDX-License-Identifier: MIT

# Exercise 4: Can You Float This For Me?
# Write a program that has a function named float_total that:
# 
# Will take a comma separated string of floats
# 
# Return a list of the floats

import argparse

def float_total(floats: str) -> list[float]:
    return [float(x) for x in floats.split(",")]

def run(args):
    print(float_total(args.s))

def main():
    """This program returns a list of floats
    """
    ap = argparse.ArgumentParser()
    ap.add_argument("s", type=str, help="Comma separated list of floats")
    args = ap.parse_args()

    run(args)

if __name__ == "__main__":
    main()
