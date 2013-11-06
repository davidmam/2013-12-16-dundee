
FILE = open("textfile", "r")

lines = FILE.readlines()

for i in range( len(lines), 0, -1 ):
    print lines[i-1],
