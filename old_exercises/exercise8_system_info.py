#! /usr/bin/env python3.8

"""
This program retrieves system information and prints it to the user

Create a program to display the following system information:
- Environmental information
- MAC address information
- Host information
- Platform information
- Current CPU usage
----- psutil.cpu_percent(<seconds to test - use 5>)
- Percentage of virtual memory in use
----- psutil.virtual_memory()[2]
- Directory and sub-directory information (full path, filename, file
size in KBytes)
----- Verify that the path is valid
----- Function should be defaulted to '' for the input path here and the
directory passed in when called
- Program must display
----- start of the program
----- end of the program
----- duration of the program when execution completes

Example Output (extra newline characters are for display purposes):
exercise8_system_info.py
Scan started at 2022-01-07 23:09:05.260910
------------------------------
The environmental variable information found is:
SHELL                         : /bin/bash
SESSION_MANAGER               : local/thekeeper:@/tmp/.ICE-unix
2012,unix/
thekeeper:/tmp/.ICE-unix/2012
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
PWD                           : /home/user/git_repos/170A_WOBC/Python/
Instructor_Resources/Instructor_Only/Graded_Exercise_Solutions
LOGNAME                       : user
XDG_SESSION_DESKTOP           : ubuntu-wayland
XDG_SESSION_TYPE              : wayland
MANPATH                       : :/home/user/man/man1
XAUTHORITY                    : /run/user/1006000561/
.mutter-Xwaylandauth.Y4WPF1
GJS_DEBUG_TOPICS              : JS ERROR;JS LOG
HOME                          : /home/user
USERNAME                      : user
IM_CONFIG_PHASE               : 1
LANG                          : en_US.UTF-8
LS_COLORS                     : rs=0:di=01;34:ln=01;36:mh=00:pi=40;
33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;
43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;
31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;
31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;
31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;
31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;
31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;
31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;
31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;
31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;
35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;
35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;
35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;
35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;
35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;
35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;
35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;
35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;
36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;
36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;
36:*.xspf=00;36:
XDG_CURRENT_DESKTOP           : ubuntu:GNOME
VTE_VERSION                   : 6003
WAYLAND_DISPLAY               : wayland-0
GNOME_TERMINAL_SCREEN         : /org/gnome/Terminal/screen/
b51e72df_d494_42ad_a8dc_d84fb926d8d4
INVOCATION_ID                 : 0bbe1b3a613e488696c370d2d9bcedae
MANAGERPID                    : 1860
GJS_DEBUG_OUTPUT              : stderr
GNOME_SETUP_DISPLAY           : :1
LESSCLOSE                     : /usr/bin/lesspipe %s %s
XDG_SESSION_CLASS             : user
TERM                          : xterm-256color
LESSOPEN                      : | /usr/bin/lesspipe %s
LIBVIRT_DEFAULT_URI           : qemu:///system
USER                          : user
GNOME_TERMINAL_SERVICE        : :1.101
DISPLAY                       : :0
SHLVL                         : 1
QT_IM_MODULE                  : ibus
XDG_RUNTIME_DIR               : /run/user/1006000561
JOURNAL_STREAM                : 9:49519
XDG_DATA_DIRS                 : /usr/share/ubuntu-wayland:/usr/local
share/:
/usr/share/:/var/lib/snapd/desktop
PATH                          : .:/home/user/.local/bin:/home/user/bin:
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:
/usr/local/games:/snap/bin:/usr/user/bin:/usr/bin:/home/user/wing/bin
GDMSESSION                    : ubuntu-wayland
DBUS_SESSION_BUS_ADDRESS      : unix:path=/run/user/1006000561/bus
_                             : ./exercise19_system_info.py
OLDPWD                        : /home/user

------------------------------
The MAC address information found is:
Device vendor for MAC address 48:5f:99:ce:f0:c3 is Cloud Network
Technology
(Samoa) Limited
Device vendor for MAC address c8:f7:50:3e:25:d1 is Dell Inc.

------------------------------
The host information found is:
sysname => Linux
nodename => thekeeper
release => 5.4.0-92-generic
version => #103-Ubuntu SMP Fri Nov 26 16:13:00 UTC 2021
machine => x86_64

------------------------------
The platform information found is:
System: Linux
Node Name: thekeeper
Release: 5.4.0-92-generic
Version: #103-Ubuntu SMP Fri Nov 26 16:13:00 UTC 2021
Machine: x86_64
Processor: x86_64

------------------------------
The CPU usage calulated is:
The CPU usage is:  0.9

------------------------------
The RAM memory % used is:
RAM memory % used: 22.3

------------------------------
The directory structure found is:
    /home/user/data_files/hash_values.txt    2.764 Kb
    /home/user/data_files/some_dir5/2020cas-rw.xlsx    127.253 Kb
    /home/user/data_files/some_dir5/intro-unix.ppt    670.5 Kb
    /home/user/data_files/some_dir5/intro22.ppt    134.0 Kb
    /home/user/data_files/some_dir5/
20201209112040_Creative_Writing_One_Year_2016.docx    268.188 Kb
    /home/user/data_files/some_dir5/Lecture6.ppt    713.5 Kb
    /home/user/data_files/dir1/progit.pdf    18233.826 Kb
    /home/user/data_files/dir1/hackingciphers.pdf    3818.564 Kb
    /home/user/data_files/dir1/Week 4.ppt    708.5 Kb
    /home/user/data_files/dir1/
Page_from_PythonCourse_Windows.pdf    104.352 Kb
    /home/user/data_files/other4/
writing handbook august 8 2019.docx    4302.48 Kb
    /home/user/data_files/other4/Orders.txt    1936.758 Kb
    /home/user/data_files/other4/python_exercises.txt    50.721 Kb
    /home/user/data_files/other4/
approved_gwar_courses_by_major.xlsx    16.077 Kb
    /home/user/data_files/other4/write_functions_in_python.txt    54.012
Kb
    /home/user/data_files/dir3/lec02-structures.ppt    3360.5 Kb
    /home/user/data_files/dir3/resources-for-students-for-pd.xlsx
19.298 Kb
    /home/user/data_files/dir3/data-science-microsoft-imagine-
academy-online-learning-directory.xlsx    40.722 Kb
    /home/user/data_files/dir3/complexitypython.txt    25.405 Kb
    /home/user/data_files/dir3/
automatetheboringstuffwithpython.pdf    14531.577 Kb
    /home/user/data_files/dir3/instruction.txt    0.125 Kb
    /home/user/data_files/dir3/fluentpython.pdf    11645.509 Kb
    /home/user/data_files/other2/PMOS2e_PPT_Ch01-4web.ppt    861.0 Kb
    /home/user/data_files/other2/
Intro to Linux Systems Administration.ppt    375.5 Kb
    /home/user/data_files/other2/pythontricks.pdf    1334.317 Kb
    /home/user/data_files/other2/Intro Ch 07B.ppt    1566.5 Kb
    /home/user/data_files/other2/Intro_to_Python.pdf    3087.424 Kb


Scan started at 2022-01-07 23:09:05.260910
Scan completed at 2022-01-07 23:09:12.675251
Scan duration is 0:00:07.414341


Exercise Notes:
- The program should have the __main___ test with a main() function
that executes the code
- Use argparse to retrieve command line arguments

"""
