# swap.py - Metallurgeek - May 2017
import sys
import argparse

# Parse
parser = argparse.ArgumentParser(
description = "Swap columns in a tab separated dataset",
epilog =      "(lines having not enough columns are skipped)")
parser.add_argument("cols",
help =        "Column numbers, e.g. 3 2 1", type = int, nargs = "+")
args = parser.parse_args()

# Prepare
skip = 0 # Count skipped lines
line = sys.stdin.readline().strip() # Read line by line (for huge files)

# Search
while line: # stop on empty line

  data = line.split('	') # FIXME: handle exceptions

  if len(data) < len(args.cols):
    skip += 1 # too bad, not enough columns
  else: 
    lout = ''
    for acol in args.cols:
      lout += data[acol-1] + '	'
    sys.stdout.write(lout[:-1] + '\n')

  line = sys.stdin.readline().strip() # Read line by line (for huge files)

if skip > 0:
  sys.stderr.write(str(skip)+' lines skiped')

