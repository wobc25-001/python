# Homework
# 2
# Concepts covered:
# - Creating a function
# - User input
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

import re

def passwordValidator9000(password):
    while True:
        check = True
        if len(password) < 14:
            check = False
            print("Your password isn't long enough, make sure it's 14 characters")
            password = input("Please enter your password: ")
        elif not re.search("[A-Z]", password):
            check = False
            print("Your password needs uppercase letters")
            password = input("Please enter your password: ")
        elif not re.search("[a-z]", password):
            check = False
            print("Your password needs lowercase letters")
            password = input("Please enter your password: ")
        elif not re.search("[0-9]", password):
            check = False
            print("Your password needs numbers")
            password = input("Please enter your password: ")
        elif not re.search("[!@#$%^&*()]", password):
            check = False
            print("Your password needs one or more special characters: !@#$%^&*()")
            password = input("Please enter your password: ")
        else:
            print("Your password is very secure. You get a free donut! Just kidding, but good job.")
            break

password = input("Please enter your password: ")
passwordValidator9000(password)