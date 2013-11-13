
# File Handling in Python

First, lets start python. We will do everything using ipython, which provides a nice interactive python shell. We start ipython using the command

    $ ipython

Writing a program involves creating and manipulating data, which are held in variables. For example, you have probably used strings and numbers,

    $ a = 42
    $ b = 65
    $ a + b
    107

prints out 107. Equally

    $ a = "hello "
    $ b = "world"
    $ a + b
    'hello world'

prints out "hello world" (note we had to add an extra space after "hello").

Typing and working with variables one-by-one like this is easy, but would be very time-consuming and prone to error if we had to type in all of this data line by line. If you want to put large amounts of data into a program, then one of the best ways of doing this is to read it from a file.

## File reading

Python is great at processing text and reading and writing files. Lets type in the following;

    $ ipython
    $ FILE = open(“textfile”, “r”)
    $ lines = FILE.readlines()
    $ i = 0
    $ for line in lines:
    $     i = i + 1
    $     print “%4d: %s” % (i, line),

What you should see is that Python has printed out every line of the file, with each line preceeded by its line number. 

    1: To be, or not to be, that is the question:
    2: Whether 'tis Nobler in the mind to suffer
    3: The Slings and Arrows of outrageous Fortune,
    4: Or to take Arms against a Sea of troubles,
    5: And by opposing end them: to die, to sleep

Lets go through each line to see how Python has achieved this feat.

The first step was to open the file. You open files using the “open” command, e.g.

    FILE = open(“textfile”, “r”)

opens the file called “textfile”. The “r” tells Python to open the file for “reading”. We will use “w” later on to open 
files for “writing”.

The file is opened and a file handle object is returned, which we have assigned to the variable “FILE”. This
handle provides the means to interact with the file. We could have called it anything we want, e.g. 

    TURTLE = open(“textfile”, “r”)
    PUSSYCAT = open(“textfile”, “r”)

would open the file and return handles called “TURTLE” and “PUSSYCAT”. Note that, by convention, we tend
to use capital letters to name file handles, and, normally, you should use reasonable names (TURTLE is perhaps
not reasonable, unless it is a file containing turtle-related data?). Note also that you can open a file as
many times as you want, and attach it to as many file handles as you want, with each one acting independently.

So, what is a file handle? We can use the help provided by Python to take a look. Python provides “help” which 
can be used on any variable. Type;

    help(FILE)

    Help on file object:
    
    class file(object)
     |  file(name[, mode[, buffering]]) -> file object
     |  
     |  Open a file.  The mode can be 'r', 'w' or 'a' for reading (default),
     |  writing or appending.  The file will be created if it doesn't exist
     |  when opened for writing or appending; it will be truncated when 
     |  opened for writing.  Add a 'b' to the mode for binary files.
     |  Add a '+' to the mode to allow simultaneous reading and writing.
     |  If the buffering argument is given, 0 means unbuffered, 1 means line
     |  buffered, and larger numbers specify the buffer size.  The preferred way
     |  to open a file is with the builtin open() function.

The filehandle provides a set of functions that can be used to interact with the file. Interesting functions
are “readline” and “readlines”. Scroll down to take a look at the documentation…

     |  readline(...)
     |      readline([size]) -> next line from the file, as a string.
     |      
     |      Retain newline.  A non-negative size argument limits the maximum
     |      number of bytes to return (an incomplete line may be returned then).
     |      Return an empty string at EOF.
     |  
     |  readlines(...)
     |      readlines([size]) -> list of strings, each a line from the file.
     |      
     |      Call readline() repeatedly and return a list of the lines so read.
     |      The optional size argument, if given, is an approximate bound on the
     |      total number of bytes in the lines returned.

As you can see, “readline” reads and returns a single line from the file, e.g.

     $ FILE = open(“textfile”, “r”)
     $ line = FILE.readline()
     $ print line

     To be, or not to be, that is the question:

We can read each line, one by one, using “readline”, e.g.

     $ line = FILE.readline()
     $ print line

     Whether 'tis Nobler in the mind to suffer

     $ line = FILE.readline()
     $ print line

     The Slings and Arrows of outrageous Fortune,

We can also read lines using a loop, e.g. read the next 5 lines

     $ for i in range(0,5):
     $     line = FILE.readline()
     $     print line,

     Or to take Arms against a Sea of troubles,
     And by opposing end them: to die, to sleep
     No more; and by a sleep, to say we end
     The Heart-ache, and the thousand Natural shocks
     That Flesh is heir to? 'Tis a consummation    

Note that I put a comma at the end of the “print line,”. This comma tells Python not to automatically add
a newline character at the end of the print. Without the comma, each print would have a newline from the line read from the 
file, plus a second newline that would be added automatically by Python.

The “readlines” function reads all remaining lines in the file into a list.

    $ lines = FILE.readlines()
    $ print lines[0]

    Devoutly to be wished. To die, to sleep,

    $ print lines[1]

    To sleep, perchance to Dream; Aye, there's the rub,

    $ print lines[-1]

    Be all my sins remembered.

    $ print len(lines)

    27

So, going back to our original example…

    $ FILE = open(“textfile”, “r”)
    $ lines = FILE.readlines()
    $ i = 0
    $ for line in lines:
    $     i = i + 1
    $     print “%4d: %s” % (i, line),

you can see that we opened the file for reading, read all of the lines using “readlines”, and then 
stepped through each line, one by one in a loop, counting up the number of each line, and printing
it out together with the line number.

## Exercise

### Exercise 1a

Using what you have learned so far, write a Python program that opens “textfile”, and prints out every even line. You can test if a 
number is even using the “%” operator, e.g.

    $ if i % 2 == 0:
    $     print “%d is even” % i
    $ else:
    $     print “%d is odd” % i

This is the remainder operator, and it returns the remainder from dividing the integer (whole number) on the left by the integer
on the right.

If you get stuck, you can look at an example program [here](python_files/even_lines.py)

### Exercise 1b

Now write a Python program that opens “textfile” and prints the file in reverse, e.g. the last line is printed first, and the first
line is printed last.

If you get stuck, you can look at an example program [here](python_files/reverse_file.py)

## Line Reading

Ok, so now we can read lines from a file. How about extracting data from each line? This is done easily in Python using
the string functions, which are included in all strings (line is a string).

    $ ipython
    $ FILE = open(“textfile”, “r”)
    $ line = FILE.readline()
    $ print line

    To be, or not to be, that is the question:

    $ line.[TAB]
    line.capitalize line.expandtabs line.isdigit    line.ljust      line.rindex     line.splitlines line.upper     
    line.center     line.find       line.islower    line.lower      line.rjust      line.startswith line.zfill     
    line.count      line.format     line.isspace    line.lstrip     line.rpartition line.strip     
    line.decode     line.index      line.istitle    line.partition  line.rsplit     line.swapcase  
    line.encode     line.isalnum    line.isupper    line.replace    line.rstrip     line.title     
    line.endswith   line.isalpha    line.join       line.rfind      line.split      line.translate 

You can see that there are a large number of functions. You can explore what they do using Python “help”. The function
we are going to look at now is “split”.

    $ help(line.split)
    
    Help on built-in function split:
    
    split(...)
        S.split([sep [,maxsplit]]) -> list of strings
        
        Return a list of the words in the string S, using sep as the
        delimiter string.  If maxsplit is given, at most maxsplit
        splits are done. If sep is not specified or is None, any
        whitespace string is a separator and empty strings are removed
        from the result.

As you can see, “split” breaks up a string into a set of words based on a separating character. If no character
is provided, then a “space” is used.

    $ words = line.split()
    $ print words
    
    ['To', 'be,', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question:']

    $ print words[0]
    To

    $ print words[-1]
    question:

You can access individual letters by remembering that a string is just an array of letters. For example, 
the first letter of the line is given by

    $ print line[0]
    T

Similarly the last letter is given by

    $ print line[-1]


(note that the last letter is the newline “\n” character).

The second to last letter is given by

    $ print line[-2]
    :

How do you print the first letter for the third word? Easy

    $ print words[2][0]
    o

You can also print out substrings using the range (:) operator, e.g.

    $ print line[10:13]
    not

prints out letters (columns) 10-13 of the line.

## Exercise

### Exercise 1c

Write a Python program that prints out the last word of every line in “textfile”.

If you get stuck, an example program is [here](python_files/last_word.py)

### Exercise 1d

Write a Python program that prints out the last letter of the first word of every line in “textfile”, 
where all of the letters are printed on the same line (e.g. put a comma at the end of the print statement).

If you get stuck, an example program is [here](python_files/get_letters.py)

## Searching in files

You can use the Python string functions to search for text as well.

    $ ipython
    $ FILE = open(“textfile”, “r”)
    $ line = FILE.readline()
    $ line.[TAB]
    line.capitalize line.expandtabs line.isdigit    line.ljust      line.rindex     line.splitlines line.upper     
    line.center     line.find       line.islower    line.lower      line.rjust      line.startswith line.zfill     
    line.count      line.format     line.isspace    line.lstrip     line.rpartition line.strip     
    line.decode     line.index      line.istitle    line.partition  line.rsplit     line.swapcase  
    line.encode     line.isalnum    line.isupper    line.replace    line.rstrip     line.title     
    line.endswith   line.isalpha    line.join       line.rfind      line.split      line.translate 

    $ help(line.find)
    Help on built-in function find:
    
    find(...)
        S.find(sub [,start [,end]]) -> int
    
        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
    
        Return -1 on failure.

As you can see, “find” will return the index of the first occurance of the searched-for string in the line,
or “-1” if it cannot be found. For example,

    $ line.find(“To”)
    0

    $ line.find(“be”)
    3

    $ line.find(“bodkin”)
    -1

You can print all lines that contain a particular string by looping over the lines and using “line.find”
to search for what you want, e.g.

    $ FILE = open(“textfile”, “r”)
    $ lines = FILE.readlines()
    $ for line in lines:
    $     if line.find(“dream”) != -1:
    $         print line,

    For in that sleep of death, what dreams may come,

Note that “find” is case-sensitive. You can use the “lower” function to lowercase the line before
searching to perform a case-insensitive search, e.g.

    $ FILE = open(“textfile”, “r”)
    $ lines = FILE.readlines()
    $ for line in lines:
    $     if line.lower().find(“dream”) != -1:
    $         print line,

    To sleep, perchance to Dream; Aye, there's the rub,
    For in that sleep of death, what dreams may come,

## Exercise

### Exercise 1e

Write a Python program that finds and prints all lines from “textfile” that contain the word “sleep”. 
Print each line together with the line number, and also print out the total number of lines in the file
that contain the word “sleep”.

If you get stuck, an example program is [here](python_files/search.py)

## Writing Files

We will finish up file handling in Python by seeing how to write to files. Before, we used “open” with “r” to
open files for reading. To open a file for writing, using “open” with “w”, e.g.

    $ ipython
    $ FILE = open(“newfile”, “w”)

This has created a new file called “newfile” and has connected it to the filehandle “FILE” in “write” mode.
To write to the file, we can use the “write” function

    $ FILE.[TAB]
    FILE.close      FILE.fileno     FILE.name       FILE.readinto   FILE.softspace  FILE.writelines
    FILE.closed     FILE.flush      FILE.newlines   FILE.readline   FILE.tell       FILE.xreadlines
    FILE.encoding   FILE.isatty     FILE.next       FILE.readlines  FILE.truncate  
    FILE.errors     FILE.mode       FILE.read       FILE.seek       FILE.write   

    $ help(FILE.write)
    Help on built-in function write:
    
    write(...)
        write(str) -> None.  Write string str to file.
    
        Note that due to buffering, flush() or close() may be needed before
        the file on disk reflects the data written.

    $ FILE.write(“Hello world\n”)
    $ FILE.close()

Note that we have to add newline “\n” characters ourselves to the string, and also that we need to 
call “FILE.close()” once we have finished writing to make sure that the file is fully written to disk
(it can sometimes only be written into a temporary memory buffer, and so not be visible when you look 
at the file on the disk).

    $ cat newfile
    Hello world

Note that every time you open a file using “w”, the file will be overwritten. Be very careful, as it is
very easy to overwrite files and delete data by mistake. One way to avoid this is to open files in
“a” (append) mode. This opens the file for writing, automatically writing at the end of the file if
it already contains some data, e.g.

    $ FILE = open(“newfile”, “a”)
    $ FILE.write(“Some more text\n”)
    $ FILE.close()
    $ cat newfile
    Hello world
    Some more text

You should also note that a file can only be opened for writing by a single filehandle at a time. This
is because if it is open by two filehandles, then reading or writing from one can get mixed up with
reading and writing from another. It is very good practice to make sure that you only open a file
for writing when you need to, to write the data into the file quickly, and to then close the file as
soon as the data has been written. Note that, as you are writing strings, it is perfectly ok to write
to the string in the program, and only write the contents to the file once the string has been composed,
e.g.

    $ lines = []
    $ lines.append(“first line of data”)
    $ lines.append(“next line of data”)
    $ lines.append(“final line of data”)
    $ FILE = open(“datafile”, “w”)
    $ for line in lines:
    $     FILE.write(“%s\n” % line)
    $ FILE.close()
    $ cat datafile
    first line of data
    next line of data
    final line of data

## Exercise

### Exercise 1f

Write a program that finds every line in “textfile” that contains the word “the” and writes those lines,
together with line numbers, to the file “textfile_thelines”.

If you get stuck, an example output is [here](python_files/thelines.py)
