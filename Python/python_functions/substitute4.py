"""This is a library of functions for substituting words in text files"""

import re

def substitute(filename, new_text):
    """Substitute every word after "the" in the file "filename" with 
       the text in "new_text". Return the resulting text as an array
       of lines."""

    lines = open(filename, "r").readlines()

    for i in range(0, len(lines)):
        line = re.sub( re.compile(r"the\s(\w+)", re.IGNORECASE), "the %s" % new_text, lines[i])
        lines[i] = line

    return lines

if __name__ == "__main__":

    lines = substitute("textfile", "banana")

    for line in lines:
        print line,
