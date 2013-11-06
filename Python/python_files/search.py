
FILE = open("textfile", "r")

lines = FILE.readlines()

count = 0
i = 0

for line in lines:
    i = i + 1
    if line.lower().find("sleep") != -1:
        count = count + 1
        print "%4d: %s" % (i, line),

print "Total number of lines equals %d" % count

