#!/usr/bin/env python3.8

"""
This program conducts a port scan on an individual IPv4 address
or a list of IPv4 addresses provided in a file, one per line

Create an IPv4 port scanner in Python that:
- Retrieves an IP list either from:
----- Command line (single IP address only)
----- Prompting the user (single IP address only)
----- Passing in from a function (single IP address only)
----- Reading from a file (multiple IP addresses possible)
- Validates that the IP address is a valid IPv4 address
----- isinstance(ipaddress.ip_address(<ip address>),
ipaddress.IPv4Address)
- Scans each IP address to determine any open ports
----- Default port range to scan is 1 - 1024 (inclusive)
----- Include the ability to modify low and high ports
- Displays:
----- IP address
----- Open ports
----- The duration that it took to run the scan (times for the duration
that it took to run the scan for each individual IPv4 address as well as
the total execution duration)

Example Output:
exercise9_port_scanner.py
============================================================
Please wait, scanning IPv4 address: 192.168.4.32
----------------------------------------
Port   22: Open
Port  139: Open
Port  445: Open
Port scanning on IPv4 address 192.168.4.32 completed in: 0:00:00.029220.
Port scanning completed in: 0:00:00.032026.


Exercise Notes:
- The program should have the __main___ test with a main() function
that executes the code
- Use argparse to retrieve command line arguments

"""
