# cidr.py - Metallurgeek - Jul 2017
help = """cidr.py
 
Usage:
  cudr.py [-v | --verbose]
 
Options:
  -h --help       Show this screen.
  -v --verbose    Print ranges as ip1-ip2
"""
 
import sys
from docopt import docopt
 
args = docopt(help)

def next():
  """Return next address (parsed) or None"""
  addr = sys.stdin.readline()
  if addr:
    return(addr[:-1].split('.'))

add1 = next()
while add1:
  # TODO: if valid_ipv4(add1):

  mini = maxi = add1[3]

  add2 = next()
  while add2:

    if add1[0:3] != add2[0:3]:
      break
    maxi = add2[3]
    add2 = next()

  # set left and right part of the display
  left = ('.').join(add1)
  if    args["--verbose"]:
    rght = '-'+('.').join(add1[0:3])+'.'+str(maxi)
  elif  maxi > mini:
    rght = '-'+str(maxi)
  else: rght = ''

  print(left+rght)
  # TODO: extrapolate smallest CIDR
  # (according to some precision, e.g. /26)

  add1 = add2


