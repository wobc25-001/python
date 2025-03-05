#! /usr/bin/env python3.8

"""
This program reads the shell environmental variables and formats
them before printing them to the user


Create a program that prints the environment variables with associated
data (formatted). Line formatting:
- Format the output as the environment variable left justified within a 30
character string
- Followed directly by a colon and a space
- Followed directly by the value that the key holds
- End each line with one new line
Results should come from a callable function. Results can either be
obtained by calling the program or set up to be called from another
program when imported.

Example output (partial):
exercise3_format_environment.py
SHELL                         : /bin/bash
SESSION_MANAGER               : local/thekeeper:@/tmp/.ICE-unix/2012,
unix/thekeeper:/tmp/.ICE-unix/2012
QT_ACCESSIBILITY              : 1
COLORTERM                     : truecolor
XDG_CONFIG_DIRS               : /etc/xdg/xdg-ubuntu-wayland:/etc/xdg
SSH_AGENT_LAUNCHER            : gnome-keyring
XDG_MENU_PREFIX               : gnome-
GNOME_DESKTOP_SESSION_ID      : this-is-deprecated
LANGUAGE                      : en_US:
GNOME_SHELL_SESSION_MODE      : ubuntu
SSH_AUTH_SOCK                 : /run/user/1006000561/keyring/ssh
XMODIFIERS                    : @im=ibus
DESKTOP_SESSION               : ubuntu-wayland
GTK_MODULES                   : gail:atk-bridge


Exercise Notes:
- The program should have the __main___ test with a main() function
that executes the code
- There is no requirement to retrieve anything from the command line

"""
