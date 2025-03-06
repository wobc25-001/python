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

# SPDX-FileCopyrightText: © 2025 Spencer Rak
# SPDX-License-Identifier: MIT
#!/usr/bin/python3

import ipaddress
import random
import string


def rand_addrs(addrs: int, dupes: int) -> [str]:
    def mkdupes(addrs, n):
        dupes = []
        for _ in range(n):
            dupes.append(random.choice(addrs))
        dupes += addrs
        return dupes

    def roctet():
        n = random.randint(1, 3)
        f = None
        if n > 2:
            f = str(random.randint(1, 2))

        r = "".join([random.choice(string.digits) for _ in range(0, (2 if n == 3 else n))])
        if f:
            r = f+r
        return r

    def raddr():
        return ".".join([roctet() for _ in range(4)])

    r = [raddr() for _ in range(addrs)]
    r = mkdupes(r, dupes)
    return r


def valid_addr(a: str) -> bool:
    try:
        _ = ipaddress.IPv4Address(a)
        return True
    except ipaddress.AddressValueError as e:
        return False

def main():
    addrs = rand_addrs(addrs=200, dupes=100)

    sort = {}
    vaddrs = []

    for a in addrs:
        # Evalute each IP address for validity.
        if not valid_addr(a):
            #print(f"`{a}` is not valid")
            continue
        vaddrs.append(a)
        if a in sort.keys():
            sort[a] += 1
        else:
            sort[a] = 1

    # Print a list of all valid IP address occurences in order of appearance.
    print(vaddrs)
    # Print a set of all valid IP addresses.
    print(set(x for x in sort.keys()))
    # Print a sorted set of all unique valid IP addresses.
    print(sorted(set(x for x in sort.keys())))



if __name__ == "__main__":
    main()
