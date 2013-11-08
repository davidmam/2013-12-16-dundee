
import re

def substitute(filename):
    lines = open(filename, "r").readlines()

    for line in lines:
        line = re.sub( re.compile(r"the\s(\w+)", re.IGNORECASE), "the banana", line)
        print line,


substitute("textfile")
