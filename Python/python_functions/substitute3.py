
import re

def substitute(filename, new_text):
    lines = open(filename, "r").readlines()

    for i in range(0, len(lines)):
        line = re.sub( re.compile(r"the\s(\w+)", re.IGNORECASE), "the %s" % new_text, lines[i])
        lines[i] = line

    return lines

if __name__ == "__main__":

    lines = substitute("textfile", "banana")

    for line in lines:
        print line,
