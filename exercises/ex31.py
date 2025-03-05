# Extra Future Content: Command Line Argument Processing
# For this challenge, you need to create one function: return_parsed_args.
# It operates as follows:
# 
# o Takes no parameters.
# 
# o
# 
# Creates an ArgumentParser object with a one-line description of
# what we are doing (that is, examining a pcap).
# 
# o
# 
# Defines five optional arguments: --start, --end, —-iplist, --protocols,
# and --follow-stream.
# 
# o
# 
# Defines one positional argument, capture.
# 
# 
# Returns an argparse.Namespace instance with those six optional
# 
# arguments as attributes. (That is, return the equivalent of args from
# step 3, above--the object that results when you run parse_args on
# an ArgumentParser instance.)
# The --start optional argument:
# ¢
# 
# [s aninteger.
# 
# 
# Has a default value of 0.
# 
# 
# Should have a help field indicating this is the first packet processed
# 
# chronologic:
# 
# lexed.
# 
# If you get stuck, try copying the example declaration of --foo, shown
# above.
# 
# The --end optional argument:
# ¢
# 
# [s aninteger.
# 
# 
# Has a default value of-1.
# 
# 
# Should have a help field indicating that this is the first packet NOT
# processed chronologically and that the packets are zero-indexed.
# 
# o
# 
# If you get stuck, try copying the example declaration of --foo, shown
# above.
# 
# The --iplist optional argument:
# 
# Is Boolean.
# 
# 
# Has a default value of False.
# 
# 
# Should have a help field. We will use this parameter to list IPs in the
# capture.
# 
# o
# 
# If you get stuck, try copying the example declaration of --true,
# shown above.
# 
# The --protocols optional argument:
# 
# Is Boolean.
# 
# 
# Has a default value of False.
# 
# 
# Should have a help field. We will use this parameter to print a list of
# protocols used in the capture.
# 
# o
# 
# If you get stuck, try copying the example declaration of --true,
# shown above.
# 
# The --follow-stream optional argument:
# o
# 
# Is alist of 2 strings (we will check for correct string formatting later.)
# 
# 
# Should have a help field specifying that the proper form for inputs
# is ip1:port1 ip2:port2.
# 
# o
# 
# If you get stuck, try copying the example declaration of --bar, shown
# above.
# 
# The capture positional argument:
# 
# 
# [s astring.
# 
# 
# Should have a help field specifying that it is expected to be the file
# name for a pcap.
# 
# D
# 
