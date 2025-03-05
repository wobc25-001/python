#! /usr/bin/env python3.8

"""
This program retrieves the host information and prints it to the user

Create a program to retrieve the host information as reported by os.uname.
Print the information retrieved for these fields within the class returned
from os.uname:
- sysname
- nodename
- release
- version
- Machine
Results should come from a callable function. Results can either be
obtained by calling the program or set up to be called from another
program when imported.

Example Output:
exercise5_get_host_information.py
sysname => Linux
nodename => thekeeper
release => 5.4.0-92-generic
version => #103-Ubuntu SMP Fri Nov 26 16:13:00 UTC 2021
machine => x86_64


Exercise Notes:
- The program should have the __main___ test with a main() function
that executes the code
- There is no requirement to retrieve anything from the command line


"""
