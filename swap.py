# swap.py - Metallurgeek - June 2017
import sys
import signal
import argparse

# Parse
parser = argparse.ArgumentParser(
description = "Swap columns in a tab separated dataset",
epilog =      "(lines having not enough columns are skipped)")
parser.add_argument("cols",
help =        "Column numbers, e.g. 3 2 1", type = int, nargs = "+")
args = parser.parse_args()

# Prepare
signal.signal(signal.SIGPIPE,signal.SIG_DFL) # Avoid broken pipe error
skip = 0 # Count skipped lines

# Search
for line in sys.stdin:

  data = line[:-1].split('	')

  if len(data) < len(args.cols):
    skip += 1 # too bad, not enough columns
  else: 
    lout = ''
    for acol in args.cols:
      lout += data[acol-1] + '	'
    sys.stdout.write(lout[:-1] + '\n')

# Result
if skip > 0:
  sys.stderr.write(str(skip)+' lines skiped')

