# topn.py - Metallurgeek - May 2017
import sys
import argparse

# Parse
parser = argparse.ArgumentParser(
description = "find top n elements; lower complexity than: sort data | uniq -c | grep -gr | head -n n",
epilog =      "(standard input, stop on empty line)")
parser.add_argument("-n", type = int, default = 1,
help =        "display only lines occurring at least n times")
args = parser.parse_args()

# Prepare
freq = {}
line = sys.stdin.readline() # Read line by line (for huge files)

# Search
while line: # stop on empty line

  word = line.strip()
  if word in freq:
    freq[word] += 1
  else:
    freq[word] = 1

  line = sys.stdin.readline()   # read line by line

# Output 
for line in sorted(freq, key=freq.get, reverse=True):   # by decreasing occurrences
  if freq[line] >= args.n:
    sys.stdout.write(str(freq[line]) + '\t' + line + '\n')
  else:
    break

