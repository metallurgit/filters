# keep.py - Metallurgeek - May 2017
import sys
import argparse

# Parse
parser = argparse.ArgumentParser(
description = "Keep lines longer or shorter than threshold(s).")
parser.add_argument("--mini", type=int, help="minimum length")
parser.add_argument("--maxi", type=int, help="maximum length")
args = parser.parse_args()

if   args.mini == args.maxi == None: parser.print_help(); exit()
elif args.maxi == None:              case = 1 # keep longer than mini
elif args.mini == None:              case = 2 # keep shorter than maxi
elif args.mini <= args.maxi:         case = 3 # keep between mini and maxi
elif args.mini  > args.maxi:         case = 4 # keep except between mini and maxi
    
# Prepare
line = sys.stdin.readline().strip() # read line by line (for huge files)

# Search
while line: # stop on empty line

  long = len(line)
  
  if ((case == 1) and (long >= args.mini))                         \
  or ((case == 2) and (long <= args.maxi))                         \
  or ((case == 3) and (args.mini <= long <= args.maxi))            \
  or ((case == 4) and ((args.maxi >= long) or (args.mini <= long))):
    sys.stdout.write(line+"\n")

  line = sys.stdin.readline().strip() # read line by line

