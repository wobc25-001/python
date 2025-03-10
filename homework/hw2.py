#!/usr/bin/python3
# SPDX-FileCopyrightText: © 2025 Spencer Rak
# SPDX-License-Identifier: MIT

# Homework
# 2
# Concepts covered:
# - Creating a function
# - User input
# 
# 
# -If / else
# - String methods
# 
# Create a function to take a password as user input. Using a while loop, if the
# password is less than 14 characters, prompt the user for a password until the user
# input is 14 or more characters. Once the user types in a password of 14 or more
# characters, check the password for an uppercase, lowercase, digit, and special
# character. If the user has all elements, print out that the password is secure, else
# print out password is not secure.
# 
# Please see the below image as a sample of what your program could look like. You do
# not have to specify how many or which character sets are missing. | just wanted to
# track it during my testing.

import getpass
import string


def main():
    pw = None

    def find_char(charset, string):
        return any(map(lambda x: x in charset, string))

    print("This is the password checker. Is your password good?\n")
    while 1:
        pw = getpass.getpass()
        if len(pw) < 14:
            print("Enter 14 or more characters")
            continue
        if not find_char(string.ascii_lowercase, pw):
            print("Your password must contain a lowercase letter")
            continue
        if not find_char(string.ascii_uppercase, pw):
            print("Your password must contain an uppercase letter")
            continue
        if not find_char(string.digits, pw):
            print("Your password must contain a digit")
            continue
        if not find_char(string.punctuation, pw):
            print("Your password must contain a symbol")
            continue
        print(f"You entered\n\n`{pw}`\n\nNice password!")
        break
        

if __name__ == "__main__":
    main()
