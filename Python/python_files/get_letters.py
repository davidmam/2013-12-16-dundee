
FILE = open("textfile", "r")

lines = FILE.readlines()

for line in lines:
    words = line.split()
    print words[0][-1],

# Print out a final newline
print "\n",

