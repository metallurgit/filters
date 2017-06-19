# filters
A set of command line filters for large input files (10Gb and more)

By filter, I mean a program reading on stdin and writing on stdout. Useful when the input cannot bestored in ram, useful for piping command UNIX style. The general form is : $ prog.py args < input > output. Occasionnaly, the filter may also write on stderr.
