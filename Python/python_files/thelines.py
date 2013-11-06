
FILE = open("textfile", "r")

lines = FILE.readlines()

result = []

i = 0

for line in lines:
    i = i + 1

    if line.lower().find("the") != -1:
        result.append("%4d: %s" % (i,line))

FILE = open("textfile_thelines", "w")

for line in result:
    FILE.write(line)

FILE.close()

