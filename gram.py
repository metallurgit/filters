# gram.py - Metallurgeek - May 2017
import sys
import argparse

# Parse
parser = argparse.ArgumentParser(
description = "count occurrences of all n-grams up to length n.",
epilog =      "(standard input, one word per line, stop on empty line)")
parser.add_argument("-n", type = int, default = 2,
help =        "1 for monograms, 2 for bigrams (default), 3 for trigrams, etc.")
parser.add_argument("-m", type = int, default = 1,
help =        "display only n-grams that occur at least m times")
args = parser.parse_args()

# Prepare
span = args.n + 1	# the maximal width of n-grams
freq = {}		# the frequency (count) of n-grams
line = sys.stdin.readline().strip() # read line by line (for huge files)

# Search
while line:	# stop on empty line

  maxi = len(line)
  
  # Generate {1..n}-grams
  for init in range(maxi):
    for stop in range(init + 1, min(init + span, maxi + 1)): # +1 is important

      gram = line[init:stop]

      # Count occurrences, faster than collections.Counter()
      if gram in freq:
        freq[gram] += 1
      else:
        freq[gram] = 1

  line = sys.stdin.readline().strip()	# read line by line

# Output 
for gram in sorted(freq, key=freq.get, reverse=True):	# by decreasing occurrences
  if freq[gram] >= args.m:
    sys.stdout.write(str(freq[gram]) + '\t' + gram + '\n')
  else:
    break

