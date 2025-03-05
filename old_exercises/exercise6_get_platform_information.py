#! /usr/bin/env python3.8

"""
This program retrieves the platform information and prints it to the user

Create a program to retrieve the platform information as reported by
platform.uname.
Print the information retrieved for these fields within the class returned
from platform.uname:
- system
- node
- release
- version
- machine
- processor
Results should come from a callable function. Results can either be
obtained by calling the program or set up to be called from another
program when imported.

Example Output:
exercise6_get_platform_information.py
System: Linux
Node Name: thekeeper
Release: 5.4.0-92-generic
Version: #103-Ubuntu SMP Fri Nov 26 16:13:00 UTC 2021
Machine: x86_64
Processor: x86_64


Exercise Notes:
- The program should have the __main___ test with a main() function
that executes the code
- There is no requirement to retrieve anything from the command line

"""
