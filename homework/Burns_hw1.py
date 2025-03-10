# Homework 1
# Concepts covered:
# - User input
# - String concatenation
# 
# - String formatting
# - Variable assignment
# - Comments
# 
# - Mathematical Operators
# 
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

#! /usr/bin/python3

import datetime

age = input("Please input your age: ") # ask user for age
fName = str(input("Please input first name: ")) # ask user for first name
lName = str(input("Please input last name: ")) # ask user for last name

def calcAge(age): # import provided age
    birthYear = datetime.datetime.now().year - int(age) # using datetime, calculate approximate birth year
    print("Your approximate birthyear is: " + str(birthYear) + "-" + str(birthYear + 1)) # output appx birth year

def possibleUsernames(first,last): # import first and last names
    firstInitialLower = first[0].lower() # lowercase first initial
    firstNameLower = first.lower() # first name all lowercase
    lastNameLower = last.lower() # last name all lowercase
    lastNameTitle = last.title() # last name titlecase
    firstInitialLastLower = firstInitialLower + lastNameLower
    camelCase = firstInitialLower + lastNameTitle
    fullLower = firstNameLower + lastNameLower
    print("Your possible usernames are: " + firstInitialLastLower + ", " + camelCase + ", " + fullLower) # output possible usernames

def hiSchool(age): # feed in age
    birthYear = datetime.datetime.now().year - int(age)
    print("Your approximate year of graduation is: " + str(birthYear+ 17) + "-" + str(birthYear + 18)) # give approximate year they graduated, based on most high school graduates graduating at 17 to 18 years old

def email(first,last):
    firstInitialLower = first[0].lower()
    firstNameLower = first.lower()
    lastNameLower = last.lower()
    lastNameTitle = last.title()
    firstInitialLastLower = firstInitialLower + lastNameLower
    camelCase = firstInitialLower + lastNameTitle
    fullLower = firstNameLower + lastNameLower
    print(f"Your possible email addresses are: {firstInitialLastLower}@gmail.com, {camelCase}@gmail.com, or {fullLower}@gmail.com") # output possible email addresses

def deathCalc(age):
    avgLifeExpectancy = 73.4 # establish average life expectancy
    percentageLived = ((int(age))*100)/avgLifeExpectancy # calculate the percentage of life lived so far
    roundedPercent = str(round(percentageLived,2)) # round that result to two decimal places
    print(f"You have lived about {roundedPercent}% of your life") # output to stdout

calcAge(age)
possibleUsernames(fName,lName)
hiSchool(age)
email(fName,lName)
deathCalc(age)