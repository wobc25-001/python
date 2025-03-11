#!/usr/bin/python3
# SPDX-FileCopyrightText: © 2025 Spencer Rak
# SPDX-License-Identifier: MIT

# Homework 4
# 
# 
# Concepts covered:
# - file input/output
# - string formatting
# - string methods
# - mathematical operations
# 
# Create program that:
# 
# Reads a filename from the command line.
# 
# Determines the most common letter in the file that is not the white space
# 
# characters, and prints what it is and how many times it occurs. Use the format
# " is the most common letter. It occurs _times." Replace _ with the appropriate
# letter (uppercase) and number. Case is important.
# e
# 
# Determines what percentage of the number of words in the file is the word
# "the"; print the percentage to two points of decimal precision. Ignore
# capitalization: "The" and "the" are the same word.
# 
# e
# 
# Writes the first ten words of the file (as determined by whitespace) to a new file
# 
# named "ten_words.txt". Assume the file will be written to the same directory
# where your program is located.

import string


def main():

    fp = None

    while 1:
        fp = input("Enter a filename: ")
        if fp not in ("small", "large"):
            print("Sorry, only files `small` and `large` are supported")
            continue
        break

    tot_words = 0
    words = {}
    freq = {}
    buf = ""

    with open(fp) as fh:
        while buf := fh.read(1024):
            for c in buf:
                if c == " ":
                    continue
                if c not in freq.keys():
                    freq[c] = 0
                freq[c] += 1
        fh.seek(0)
        for l in fh.readlines():
            for w in map(str.lower, l.strip().split(" ")):
                if len(w) == 0:
                    continue
                if w[0] in string.punctuation:
                    w = w[1:]
                if w[-1] in string.punctuation:
                    w = w[:-1]
                tot_words += 1
                if w not in words:
                    words[w] = 0
                words[w] += 1

    print(freq)
    print(words)
    print(tot_words)


if __name__ == "__main__":
    main()
