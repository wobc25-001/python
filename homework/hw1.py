#!/usr/bin/python3
# SPDX-FileCopyrightText: © 2025 Spencer Rak
# SPDX-License-Identifier: MIT

# Homework 1
# Concepts covered:
# - User input
# - String concatenation
# - String formatting
# - Variable assignment
# - Comments
# - Mathematical Operators
# - Floats
# 
# Create a program that accepts the age, first name, and last name of the user as user
# input.
# 
# The program should then print:
# 
# 1. A sentence that states the user's birthyear.
# 2. 3 possible username formats based on their first name and last name.
# 3. 2 possible years the user might have graduated high school.
# 4. 3 possible "@gmail.com" email addresses based on the previous identified
# username formats.
# 5. Percentage of life completed based on life expectancy of 73.4.
# General requirements for the program:
# 1. Shebang so it can be run by executing the file
# 2. Use both string concantenation and string formatting at least once.
# 3. Use appropriate variables to assign your values.
# 4. Use appropriate comments to explain how your program is functioning.
# 5. Name your file "Iname_hw1.py"

import datetime
now = datetime.datetime.now()


def tombstone(age, name) -> None:
    bd = 2025-age
    dd = datetime.datetime(bd, now.month, now.day)
    d = now.strftime("%m/%d/%Y")
    b = dd.strftime("%m/%d/%Y")
    print("We are sorry, you seem to have exceeded the average life expectancy of 73.4y\n\n")
    stone = "                                 _____  _______\n"
    stone += "                                <     `/       |\n"
    stone += "                                 >            (\n"
    stone += "                                |   _     _    |\n"
    stone += "                                |  |_) | |_)   |\n"
    stone += "                                |  | \ | |     |\n"
    stone += "                                |              |\n"
    stone += "                 ______.______%_|              |__________  _____\n"
    stone += "               _/                                         \|     |\n"
    stone += f"              |                   {name}              <\n"
    stone += "              |_____.-._________                __/|_____________|\n"
    stone += f"                                | * {d} |\n"
    stone += f"                                | + {b} |\n"
    stone += "                                |              |\n"
    stone += "                                |              |\n"
    stone += "                                |   _          <\n"
    stone += "                                |__/           |\n"
    stone += "                                 / `--.        |\n"
    stone += "                               %|              |%\n"
    stone += "                           |/.%%|            -< @%%%\n"
    stone += "                           `\%`@|     v        |@@%@%%    - mfj\n"
    stone += "                         .%%%@@@|%    |    % @@@@@%%@%%%%\n"
    stone += "                    _.%%%%%%@@@@@@%%_/%\_%@@%%@@@@@@@@@%%%%%%\n"
    print(stone)


def loading_bar(p: float) -> None:
    """Given a percentage display a bar
    Example:
        [=======-    ]
    """
    e = int(p // 4)
    d = p % 4
    # we fit the percentage to our bar
    # we choose to use a bar with 25 positions
    # a position is an `=` if the bucket is "full"
    # a position is a `-` if it is partial
    line = "["
    line += (e * "=")
    line += "-" if d > 0 else ""
    line += (25-e-(1 if d else 0)) * " "
    line += "]"
    print(line)

def unames(first, last):
    first, last = map(str.lower, (first, last))
    return (
        first[0]+"."+last,
        first+"."+last,
        first+"."+last[0],
    )

def main():
    age = None
    name = None

    while 1:
        try:
            age = input("Enter your age: ")
            age = int(age)
            break
        except ValueError as e:
            print("Please enter a number.")

    fname = input("Enter your first name: ").strip().title()
    lname = input("Enter your last name: ").strip().title()

    p = (1 - (73.4 - age) / 73.4) * 100

    print("\n")

    print(f"The users's birthyear is: {now.year-age}")
    lunames = unames(fname, lname)
    print(lunames)
    print(f"You probably graduated highschool in {now.year-age+18}.")
    print(f"Your possible email addresses are "+", ".join(map(lambda x: f"{x}@gmail.com", lunames)))

    print("\n")

    if p > 100:
        tombstone(age, fname+" "+lname)
    else:
        print(f"Congratulations: {fname} {lname} You have completed {p:.2f}% of your journey.")
        loading_bar(p)

    print("\n")

if __name__ == "__main__":
    main()
