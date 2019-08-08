#!/usr/bin/python3
'''
Fold lists of integers or IPv4 addresses into intervals. And converse.

Usage:
    fold.py

Examples:
    $ seq 25 36 | fold.py
    25~36
    $ echo "127.0.0.3~127.0.0.5" | fold.py | tr "\\n" " "
    127.0.0.3 127.0.0.4 127.0.0.5

Remarks:
    x~y stands for all items i such that x <= i <= y.
    No more than one item per line, lines with no item are discarded.
    Sorted inputs give better results (cf. sort -g and sort -V).
'''

from sys        import stdin    as STDI
from docopt     import docopt   as args

BYTE = range(256)

def item2numb(text):
    '''If text corresponds to an int or an IPv4, convert it to number and type'''
    try:
        if '.' in text:                                         # Maybe it's an IPv4
            byt1, byt2, byt3, byt4 = map(int, text.split('.'))  # Need exactly four int
            if byt1 in BYTE and byt2 in BYTE and byt3 in BYTE and byt4 in BYTE:
                return (((byt1*256)+byt2)*256+byt3)*256+byt4, True
        else:                                                   # Maybe it's an int
            return int(text), False
    except ValueError:
        pass
    return None, False                                          # Maybe it's irrelevant

def show_item(isip, init, stop=None):
    '''Show an item or an interval according to its type'''

    def show(isip, numb):                                       # Inner auxil. function
        '''Convert an item to a string according to its type'''
        if isip:
            return '{}.{}.{}.{}'.format((numb//256**3)%256,     \
            (numb//256**2)%256, (numb//256)%256, numb%256)
        return str(numb)

    print(show(isip, init), end='')                             # Print a value
    if stop is not None:
        if stop > init:
            print('~'+show(isip, stop), end='')                 # And maybe an interval
    print()

ARGS = args(__doc__)                                            # Parsing command line
SEEN = False                                                    # No item already seen
TYPE = False                                                    # A priori we expect int
INIT = STOP = ITEM = None                                       # Values are yet unknown

for LINE in STDI:                                               # MAIN PROGRAM LOGIC
    if '~' in LINE:                                             # Maybe it's an interval
        try:
            x, y = LINE.split('~')                              # Need exactly two values
            list_init, list_type = item2numb(x)                 # First item gives type
            list_stop, _ = item2numb(y)
            for i in range(list_init, list_stop+1):
                show_item(list_type, i)                         # Print items in interval
        except (ValueError, TypeError):
            pass                                                # It was not an interval
    else:                                                       # Maybe it's just an item
        ITEM, ISIP = item2numb(LINE)
        if ITEM is not None:                                    # Do we have an item?
            if SEEN:
                if ITEM == STOP+1:                              # Well-ordered next item
                    STOP += 1                                   # Increment the interval
                    continue                                    # Nothing else to do
                show_item(TYPE, INIT, STOP)                     # Display the item and
            INIT = STOP = ITEM                                  # Start the first interval
            TYPE = ISIP                                         # With same type as item
            SEEN = True                                         # Note an item was seen

if SEEN:                                                        # Handle 1 or 2 line files
    show_item(TYPE, INIT, STOP)
