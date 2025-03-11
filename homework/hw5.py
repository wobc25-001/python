#!/usr/bin/python3
# SPDX-FileCopyrightText: © 2025 Spencer Rak
# SPDX-License-Identifier: MIT

# Homework 5
# Concepts covered:
# - regular expressions
# 
# - string splitting OR
# - capture groups
# 
# Write a python program that takes a file name as a command line argument that will:
# 1. Counts the number of lines ending in a "?". You will print that value, followed by all
# of the sentences.
# 2. Find all phone numbers and print them to the screen. Format for phone numbers
# 
# should all be 706-123-4567.
# 3. Find all ".com" email addresses in the file. Print their username and the email
# domain. Format should be: kirk.carter uses gmail.com

import argparse
import csv
import random
import string


def generate():
    def remail():
        return random.choice((
            "gmail.com",
            "yahoo.com",
            "microsoft.com",
            "icloud.com",
            "dod.gov",
            "army.mil",
            "mypay.mil",
            "ubiquitipainters.net",
            "tombradyphotographers.org",
        ))

    def rchar():
        return random.choice(("_", ".", "-"))

    def rphone():
        def rnum(n):
            return "".join([random.choice(string.digits) for _ in range(n)])
        f = rnum(3)
        m = rnum(3)
        l = rnum(4)
        if f.startswith("0"):
            f = f"1{f[1:]}"
        if m.startswith("0"):
            m = f"1{m[1:]}"
        if l.startswith("0"):
            l = f"1{l[1:]}"
        return f"{f}-{m}-{l}"

    fh = open("customers.csv")
    wfh = open("emails.txt", "w")
    wfh.write("Email,Phone Number\n")
    cr = csv.reader(fh)
    # skip the header
    _ = next(cr)
    while 1:
        try:
            row = next(cr)
        except StopIteration as e:
            break
        if len(row) != 8:
            continue
        _, fname, lname, _, _, _, _, _ = tuple(map(str.lower, row))
        email = f"{fname}{rchar()}{lname}@{remail()}"
        phone = rphone()
        wfh.write(email+","+phone+"\n")
    fh.close()
    wfh.close()


def run():
    ...

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--generate", help="Generate junk test data", action="store_true")
    args = ap.parse_args()

    if args.generate:
        generate()
    else:
        run()
        

if __name__ == "__main__":
    main()
