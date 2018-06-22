import sys
import os
import re
import optparse
import time
import getpass
import readline
import atexit
try:
    import pexpect
    import pxssh
except ImportError:
    sys.stderr.write("You do not have 'pexpect' installed.\n")
    sys.stderr.write("On Ubuntu you need the 'python-pexpect' package.\n")
    sys.stderr.write("    aptitude -y install python-pexpect\n")
    exit(1)
