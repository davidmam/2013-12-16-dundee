import sys

filename = sys.argv[1]

FILE = open(filename, "r")

lines = FILE.readlines()

i = 0

for line in lines:
    i = i + 1
    print "%4d: %s" % ( i, line ),
