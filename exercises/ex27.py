# Exercise 27
# The purpose of this program is to retrieve the MAC address for all interfaces found on
# the host system, retrieve the vendor that supplied the interface, and prints the results
# in a formatted way. The program will:
# only execute commands if execution occurred as a result of this program name
# being called and not when imported
# when imported, functions will only execute when called
# 
# create a function called main that will call the other functions to perform the
# required actions
# create a function called get_if_name_list
# o
# 
# is passed in the file name to retrieve the interface names
# =
# 
# /proc/net/dev
# 
# read the file
# look for colons (:), skipping lines with colons
# retrieve the name before the colon (:)
# return the list of interface names found
# 
# create a function called get_mac_addresses
# is passed in a list of interface names
# for each interface name
# opens an empty socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 
# retrieves the MAC address associated with the socket for the
# specified interface name
# 
# =
# 
# retrieve the information associated with the interface name's
# 
# socket
# m
# 
# fentlioctl(sock.fileno(), 0x8927, struct.pack('256s',
# 
# »
# 
# <if_name_variable>get the MAC address from the information
# 
# m
# 
# <if_name_variable>"".join('%02x' % b for b in <var_name>[18:24])
# 
# ®
# 
# <if_name_variable><var_name>close the socket
# 
# »
# 
# <if_name_variable><var_name>keep the recovered MAC address
# 
# bytes(<if_name_variable><if_name_variable>,'utf-8')[:15]))
# 
# recovered
# 
# if it is not '00:00:00:00:00:00'
# m
# 
# <if_name_variable><var_name>return the recovered list of MAC
# 
# addresses found
# e
# 
# create a function called get_mac_details
# o
# 
# is passed in a list of mac_addresses
# 
# o
# 
# to retrieve MAC address vendor, use the API url
# 
# ©
# 0O
# 
# sleep for 1 second, required for API to ensure that it works
# 
# O
# 
# 0O
# 
# 0O
# 
# 0O
# 
# 0O
# 
# append the MAC address to the API url
# 
# 0O
# 
# of:https://api.macvendors.com/
# step through each MAC address found
# 
# use the requests library to read data from the API
# requests.get
# 
# requests.status_code (200 is a valid response)
# requests.content.decode
# if a valid response was received, store the MAC address with the vender
# decoded from the response
# if a valid response was not received, store the MAC address with the
# phrase "[!] Invalid MAC Address"
# return dictionary of the the MAC address with the associated
# information stored
# 
# e
# 
# create a function called print_mac_address_info
# o
# 
# is passed in the dictionary of MAC address with associated information
# 
# O
# 
# step through each MAC address found
# 
# O
# 
# if the MAC address was valid, print the message formatted:
# 
# O
# 
# Device vendor for MAC address is .
# 
# O
# 
# stored
# 
# if the MAC address was invalid, print the message formated:
# =
# 
# [1] Invalid MAC Address:
# 
# Example Output (extra newline characters are for display purposes only):
# exercise4_mac_information.py
# Device vendor for |
# 
# 1C..
# 
# https://cybercoe.lic.army.mil/webapps/blackboard/content/listContent.jsp?course
# _id= 7410 1&content _id=
# 
# 1403351
# 1
# 
# 17/21
# 
# 3/5/25,10:17 AM
# 
# 
# Device vendor for MAC address 48:5f:99:ce:f0:c3 is Cloud NetworkTechnology
# (Samoa) Limited.
# Exercise Notes:
# e
# 
# The program should have the __main__test with a main() function that
# 
# e
# 
# There is no requirement to retrieve anything from the command line
# 
# ¢
# 
# Functions must be named exactly as listed above
# 
# e
# 
# Output must be identically formatted as to what is shown here
# 
# executes the code
# 
# Grading: Grading will be based upon whether the requirements are met and if the
# code executes without errors or warnings to complete the requirements. Partial
# credit may be granted, if code is there to support it when a requirement has not been
# met. The submitted program must work with python3.8 and on the classroom
# machine.
# # Imports the modules
# 
# def get_if_name_list():
# pass
# 
# def get_mac_addresses():
# pass
# 
# def get_mac_details():
# pass
# 
# def print_mac_address_info():
# pass
# 
# def main():
# pass
# 
# if _name__=="_main__":
# pass
# 
