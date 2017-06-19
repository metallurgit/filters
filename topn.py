# topn.py - Metallurgeek - June 2017
import sys
import argparse

# Parse
parser = argparse.ArgumentParser(
description = "find top n elements; like sort data | uniq -c | grep -gr | head -n n")
parser.add_argument("-n", type = int, default = 1,
help =        "display only lines occurring at least n times")
args = parser.parse_args()

# Prepare
freq = {}

# Search
for line in sys.stdin:

  word = line.strip()
  if word in freq:
    freq[word] += 1
  else:
    freq[word] = 1

# Output 
for word in sorted(freq, key=freq.get, reverse=True):   # by decreasing occurrences
  if freq[word] >= args.n:
    sys.stdout.write(str(freq[word]) + '\t' + word + '\n')
  else:
    break

