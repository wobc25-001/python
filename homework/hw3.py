# Homework 3
# Concepts covered:
# - dictionaries
# - set
# 
# - list
# - iterable methods
# 
# - conditionals
# - Simple checking OR
# - Regular expressions
# - For loops
# 
# addresses = (
# '192.168.254.1",
# 
# '867.53.0.9,
# '192.168.254.1",
# 
# '255.255.255.257',
# '10.10.100.1",
# "172.16.0.1',
# '192.168.254.1",
# 
# '10.10.100.2,
# '8.8.8.8/,
# '"1337.4150.4444.07
# 
# )
# Write a program that uses the above tuple of IP addresses to:
# 
# Print a dictionary with each IP address as the key and the count of occurences of each
# 
# IP address in the tuple as its value.
# Evalute each IP address for validity.
# Print a list of all valid IP address occurences in order of appearance.
# Print a set of all valid IP addresses.
# Print a sorted set of all unique valid IP addresses.

# SPDX-FileCopyrightText: © 2025 Spencer Rak
# SPDX-License-Identifier: MIT
#!/usr/bin/python3

import random
import string

def roctet():
    n = random.randint(1, 3)
    f = None
    if n > 2:
        f = str(random.randint(1, 2))

    r = "".join([random.choice(string.digits) for _ in range(0, (2 if n == 3 else n))])
    if f:
        r = f+r
    if int(r) > 255:
        r = "255"
    return r


def raddr():
    return ".".join([roctet() for _ in range(4)])

def raddrs(x):
    return [raddr() for _ in range(x)]

def mkdupes(addrs, n):
    dupes = []
    for _ in range(n):
        dupes.append(random.choice(addrs))
    dupes += addrs
    return dupes

def main():
    addrs = raddrs(100)
    addrs = mkdupes(addrs, 100)

    sort = {}

    for a in addrs:
        if a in sort.keys():
            sort[a] += 1
        else:
            sort[a] = 1

    print(sort)



if __name__ == "__main__":
    main()
