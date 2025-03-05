#! /usr/bin/env python3.8

"""
This program walks through a starting directory finding all the files and
printing them along with their associated file size in KBytes

Create a program that will, from the base directory provided, display the
file (with full path) and its file size in KBytes for all files in this
directory as well as all sub-directories.
Allow required arguments to be set via:
- **kwargs
- command line (argparse)
- manually by prompting (if valid value not entered through either of the
other two entry points)
Perform the following actions
- Change directory to the directory specified
- Perform a walk of the directories (os.walk)
- Retrieve the full path with file name as well as the size of all files
that are readable by the user
- All file sizes should be formatted as kilobytes (KBytes) - Rounded to
three decimal places:
----- f{'round(os.stat(<file name>).st_size/(1024),3)} Kb‘
- Display a message stating that these are the files found
- For each file information line, begin it with a tab and separate the
filename from the file size with a tab
Results should come from a callable function. Results can either be
obtained by calling the program or set up to be called from another
program when imported.

Example Output:
exercise7_directory_walk.py -b /data/Python
The directory structure found is:
    /data/Python/Python_Tricks.pdf	1334.317 Kb
    /data/Python/Fluent_Python.pdf	11645.509 Kb
    /data/Python/Automate_the_Boring_Stuff_with_Python.pdf	14531.577 Kb
    /data/Python/Python_Learn_Python_The_Hard_Way_2nd_Ed.pdf	750.785 Kb
    /data/Python/Python_Crash_Course_2nd_Edition.pdf	7529.984 Kb
    /data/Python/Intro_to_Python.pdf	3087.424 Kb
    /data/Python/Hacking_Ciphers.pdf	3818.564 Kb


Exercise Notes:
- The program should have the __main___ test with a main() function
that executes the code
- Use argparse to retrieve command line arguments

"""
