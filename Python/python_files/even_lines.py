
FILE = open("textfile", "r")

lines = FILE.readlines()

i = 0

for line in lines:
    if i % 2 == 0:
        print line,

    i = i + 1

