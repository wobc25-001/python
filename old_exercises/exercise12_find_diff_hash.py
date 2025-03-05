#! /usr/bin/env python3.8

"""
This program walks a directory structure to calculate the MD5 and SHA1
hash for each file. It then reads a file that contains either a MD5 or
SHA1 hash for the same files that were calculated previously. It then
performs a comparison between the hashes read from the file to the ones
calculated.
If any of the hashes differ, the file name and differences are displayed
to the user.

Create a program to find the changed file.
The hash_values.txt file contains either the MD5 or SHA1 hash for all the
files found in the provided base directory. Traverse the base directory to
calculate the same hash type as found in the hash_values.txt file for each
of the files found (excluding hash_values.txt). Compare the calculated
value to what is stored in the hash_values.txt file to identify the file
that has a different hash file. This indicates that the file has been
modified since the hash value was stored in the hash_values.txt file.

Example Output:
exercise12_find_diff_hash.py -f /data_files/hash_file.txt -b /data_files
File with incorrect hash found: /data_files/this_dir/somefile.txt
    Hash type found md5
    Hash value calculated:     cf3b659fd388d5fbfc02da3b4b311537
    Hash value read from file: 4dd22932bd09f3b35d947c3fc943e789


Exercise Notes:
- The program should have the __main___ test with a main() function
that executes the code
- Use argparse to retrieve command line arguments

"""
