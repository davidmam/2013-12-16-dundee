
import re

lines = open("textfile", "r")

for line in lines:
    line = re.sub( re.compile(r"the\s(\w+)", re.IGNORECASE), "the banana", line)
    print line,

