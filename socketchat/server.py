# SPDX-FileCopyrightText: © 2025 Spencer Rak
# SPDX-License-Identifier: MIT

import asyncio
import logging
import random
import socket


from socketchat.config import logconfig


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--client", help="Generate junk test data", action="store_true")
    ap.add_argument("-v", dest="verbose", help="Increase logging", action="count")
    args = ap.parse_args()

    if args.generate:
        generate()
    else:
        run()
    print(args.verbose)
    breakpoint()
        

if __name__ == "__main__":
    main()
