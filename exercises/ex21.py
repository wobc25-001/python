# Exercise 21: Password Checker
# Create a program named password_checker with a function
# named password_checker that:
# Takes one string argument (password)
# 
# Checks the password for the following rules:
# 
# Password must be at least 14 characters in length
# Password must contain at least one character from each of the following
# four character sets:
# 
# Uppercase characters (string.ascii_uppercase)
# Lowercase characters (string.ascii_lowercase)
# Numerical digits (string.digits)
# Special characters (string.punctuation)
# 
# Password cannot contain more than three consecutive characters from the
# same character set.
# 
# Password cannot contain whitespace characters (string.whitespace)
# 
# Returns True if a valid password. False, otherwise.
# 
# You will test your program with the testpasswords.pyc:
# 
# >>> python3 testpasswords.pyc --module password_checker.py --checker
# password_checker
