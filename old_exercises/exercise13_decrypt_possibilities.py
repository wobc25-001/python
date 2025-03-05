#! /usr/bin/env python3.8

"""
This program is designed attempt to decrypt a file with a generated four
digit passcode.

Create a program that uses file_encrypt_decrypt.cpython-38.pyc to attempt
the decryption of the file found in Exercise 12.

Use 1200 as the starting value and 1300 (inclusive) as the stopping value
for the password.

Output:
exercise13_decrypt_possibilities.py -p file_encrypt_decrypt.cpython-38.pyc
-f <somefile>.<end> -b <somefile><_extension> -lp 1200 -hp 1300
Will produce a decrypted file, if the correct password is provided
<somefile><_extension><_password>.txt

Exercise Notes:
- The program should have the __main___ test with a main() function
that executes the code
- Use argparse to retrieve command line arguments

"""
