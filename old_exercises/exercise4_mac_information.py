#! /usr/bin/env python3.8

"""
This program retrieves the MAC address information from the system

Create a program to read the MAC addresses on the local machine to
determine the vendor.
- Determine the ethernet names on the device (/proc/net/dev)
- Determine the MAC address associated with the ethernet device
----- fcntl.ioctl(<open socket>.fileno(), 0x8927, struct.pack('256s',
bytes(<ethernet device>, 'utf-8')[:15]))
- Format the MAC address (00:00:00:00:00:00 is an invalid MAC address and
should be skipped)
----- ':'.join('%02x' % b for b in <fcntl.ioctl output>[18:24])
- Retrieve the vendor
----- API to retrieve vendor, if valid MAC address and exists in the APIs
database:     https://api.macvendors.com/
- Use the requests library to read data from the API (must sleep for 1
second before each API call)
----- requests.get
----- requests.status_code
----- requests.content.decode
- Display the MAC address with its vendor (within a callable function)
Results should come from a callable function. Results can either be
obtained by calling the program or set up to be called from another
program when imported.

Example Output (extra newline characters are for display purposes only):
exercise4_mac_information.py
Device vendor for MAC address 48:5f:99:ce:f0:c3 is Cloud Network
Technology
(Samoa) Limited
Device vendor for MAC address c8:f7:50:3e:25:d1 is Dell Inc.

Exercise Notes:
- The program should have the __main___ test with a main() function
that executes the code
- There is no requirement to retrieve anything from the command line

"""
