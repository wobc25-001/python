#! /usr/bin/env python3.8

"""
This program starts from a base directory and walks through all the
sub-directories to calculate the md5 and sha1 hash values for each
of the files found

Create a program to traverse a directory structure to produce the hash
for each file that is readable by the user.
- Conduct a directory walk
- Create the requested hash for each readable file found
- Display the requested hash with the file

Example Output (extra newline characters for display purposes only):
exercise11_get_file_hashes.py -b /data/Python
/data/Python/.gitkeep:MD5:d41d8cd98f00b204e9800998ecf8427e
/data/Python/.gitkeep:SHA1:da39a3ee5e6b4b0d3255bfef95601890afd80709
/data/Python/Python_Tricks.pdf:MD5:62b07ad2dce02ee67e05cba41e9146b8
/data/Python/
Python_Tricks.pdf:SHA1:3ec75c179b6df168d591e89b5a53cf94d7e60ab9
/data/Python/Fluent_Python.pdf:MD5:9188331e5b8410ad16c202e095adf622
/data/Python/
Fluent_Python.pdf:SHA1:64ab35870db826d8e34d048b9f9ce75c97bd133a
/data/Python/Automate_the_Boring_Stuff_with_Python.pdf:MD5:
4dd22932bdaae6b35d947c3fc943e789
/data/Python/Automate_the_Boring_Stuff_with_Python.pdf:SHA1:
7f6ba84b08166fded19289e8eaa69bbda156614d
/data/Python/Python_Learn_Python_The_Hard_Way_2nd_Ed.pdf:MD5:
c0c5a7800351ebd7cc42eed6e244d0a4
/data/Python/Python_Learn_Python_The_Hard_Way_2nd_Ed.pdf:SHA1:
4e268425bb66bcee7ed85f8f996e94e8b7d88df7
/data/Python/Python_Crash_Course_2nd_Edition.pdf:MD5:
cef1eef37d56c78769449714208116f9
/data/Python/Python_Crash_Course_2nd_Edition.pdf:SHA1:
0e9d23ee0aea2da57e59d32c8e8da561187acb8f
/data/Python/Intro_to_Python.pdf:MD5:8721e7ce0c925b74433b654a0dbe2911
/data/Python/
Intro_to_Python.pdf:SHA1:260f0ad51a8d44e55ef222c75aa29d09e440d70f
/data/Python/Hacking_Ciphers.pdf:MD5:6ee1f32a15cb14ed190f3bbd34885f21
/data/Python/
Hacking_Ciphers.pdf:SHA1:86a608336eea13ac543566fae61ab002a5c34cf3

Exercise Notes:
- The program should have the __main___ test with a main() function
that executes the code
- Use argparse to retrieve command line arguments


"""
