# SPDX-FileCopyrightText: © 2025 Spencer Rak
# SPDX-License-Identifier: MIT

import asyncio
import argparse

from socketchat import Server, Client


async def amain(args):
    if args.server:
        asyncio.run(Server().run())
    elif args.client:
        asyncio.run(Client().run())

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
