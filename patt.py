# keep.py - Metallurgeek - June 2017
import sys
import signal
import argparse

# Parse
parser = argparse.ArgumentParser(
description = "Replace symbols by patterns: [a-z]->l [A-Z]->U [0-9]->9 [other]->s")
args = parser.parse_args()

# Prepare
signal.signal(signal.SIGPIPE,signal.SIG_DFL) # Avoid broken pipe error

l = 'abcdefghijklmnopqrstuvwxyz'
U = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
d = '0123456789'

# Search
for line in sys.stdin:

  patt = ''
  for char in line.strip():
    if   char in l: patt += 'l'
    elif char in U: patt += 'U'
    elif char in d: patt += '9'
    else          : patt += 's'
  
  sys.stdout.write(patt+"\n")

