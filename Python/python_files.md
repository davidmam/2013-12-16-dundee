<h3>Using open to read a file</h3>
In Python, as in the physical world, we have to open a file before we can read what's inside it. The Python function that carries out the job of opening a file is very sensibly called <code>open</code>. It takes one argument – a string which contains the name of the file – and returns a <i>file object:</i>


    my_file = open("dna.txt")


A <i>file object</i> is a new type of data. With strings and numbers it was easy to understand what they represented – a single bit of text, or a single number. A file object, in contrast, represents something a bit less tangible – it represents a file on your computer's hard drive.

The first thing we need to be able to do is to read the contents of the file. The file type has a <code>read</code> method which does this. It doesn't take any arguments, and the return value is a string, which we can store in a variable. Once we've read the file contents into a variable, we can treat them just like any other string – for example, we can print them:


    my_file = open("dna.txt")
    file_contents = my_file.read()
    print(file_contents)


<h2>Files, contents and file names</h2>
When learning to work with files it's very easy to get confused between a <i>file object</i>, a <i>file name</i>, and the <i>contents </i>of a file. Take a look at the following bit of code:


    my_file_name = "dna.txt"
    my_file = open(my_file_name)
    my_file_contents = my_file.read()


What's going on here? On line 1, we store the string <i>dna</i><i>.txt</i> in the variable <code>my_file_name</code>. On line 2, we use the variable <code>my_file_name </code>as the argument to the <code>open </code>function, and store the resulting file object in the variable <code>my_file</code>. On line 3, we call the <code>read </code>method on the variable <code>my_file</code>, and store the resulting string in the variable <code>my_file_contents</code>.

The important thing to understand about this code is that there are three separate variables which have different types and which are storing three very different things. <code>my_file_name </code>is a string, and it stores the name of a file on disk. <code>my_file </code>is a file object, and it represents the file itself. <code>my_file_contents </code>is a string, and it stores the text that is in the file.

Remember that variable names are arbitrary – the computer doesn't care what you call your variables. So this piece of code is exactly the same as the previous example:


    apple = "dna.txt"
    banana = open(apple)
    grape = banana.read()


except it is harder to read! In contrast, the file name (<i>dna</i><i>.txt</i>) is <b>not</b> arbitrary – it must correspond to the name of a file on the hard drive of your computer.

A common error is to try to use the <code>read</code> method on the wrong thing. Recall that <code>read</code> is a method that only works on file objects. If we try to use the <code>read</code> method on the file name:


    my_file_name = "dna.txt"
    my_contents = my_file_name.read()


we'll get an <code>AttributeError</code> – Python will complain that strings don't have a <code>read</code> method:


    AttributeError: 'str' object has no attribute 'read'


Another common error is to use the <i>file object </i>when we meant to use the<i> file contents</i>. If we try to print the file object:


    my_file_name = "dna.txt"
    my_file = open(my_file_name)
    print(my_file)


we won't get an error, but we'll get an odd-looking line of output:


    <open file 'dna.txt', mode 'r' at 0x7fc5ff7784b0>


We won't discuss the meaning of this line now: just remember that if you try to print the contents of a file but instead you get some output that looks like the above, you have almost definitely printed the file object rather than the file contents.

<h2>Dealing with newlines</h2>
Let's take a look at the output we get when we try to print some information from a file. We'll use the file <i>dna.txt</i> from the repository. This file contains a single line with a short DNA sequence. Open the file up in a text editor and take a look at it.

We're going to write a simple program to read the DNA sequence from the file and print it out along with its length. Putting together the file functions and methods from this session, and the printing / string manipulation stuff from the preperation chapter, we get the following code:


    # open the file
    my_file = open("dna.txt")
    # read the contents
    my_dna = my_file.read()
    # calculate the length
    dna_length = len(my_dna)
    # print the output
    print("sequence is " + my_dna +  " and length is " + str(dna_length))


When we look at the output, we can see that the program is working almost perfectly – but there is something strange: the output has been split over two lines:


    sequence is ACTGTACGTGCACTGATC
     and length is 19


The explanation is simple once you know it: Python has included the new line character at the end of the <i>dna.txt</i> file as part of the contents. In other words, the variable <code>my_dna</code> has a new line character at the end of it. If we could view the <code>my_dna </code>variable directly (In fact, we can do this – there's a function called <code>repr</code> that returns a representation of a variable) , we would see that it looks like this:


    'ACTGTACGTGCACTGATC\n'


The solution is also simple. Because this is such a common problem, strings have a method for removing new lines from the end of them. The method is called <code>rstrip</code>, and it takes one string argument which is the character that you want to remove. In this case, we want to remove the newline character (<code>\n</code>). Here's a modified version of the code – note that the argument to <code>rstrip</code> is itself a string so needs to be enclosed in quotes:


    my_file = open("dna.txt")
    my_file_contents = my_file.read()
    # remove the newline from the end of the file contents
    my_dna = my_file_contents.rstrip("\n")
    dna_length = len(my_dna)
    print("sequence is " + my_dna +  " and length is " + str(dna_length))


and now the output looks just as we expected:

    sequence is ACTGTACGTGCACTGATC and length is 18

In the code above, we first read the file contents and then removed the newline, in two separate steps:

    my_file_contents = my_file.read()
    my_dna = my_file_contents.rstrip("\n")

but it's more common to read the contents and remove the newline all in one go, like this:

    my_dna = my_file.read().rstrip("\n")

This is a bit tricky to read at first as we are using two different methods (<code>read</code> and <code>rstrip</code>) in the same statement. The key is to read it from left to right – we take the <code>my_file</code> variable and use the <code>read</code> method on it, then we take the output of that method (which we know is a string) and use the <code>rstrip</code> method on it. The result of the <code>rstrip</code> method is then stored in the <code>my_dna</code> variable.

If you find it difficult write the whole thing as one statement like this, just break it up and do the two things separately – your programs will run just as well.

<h2>Missing files</h2>
What happens if we try to read a file that doesn't exist?

    my_file = open("nonexistent.txt")


We get a new type of error that we've not seen before:

    IOError: [Errno 2] No such file or directory: 'nonexistent.txt'


<h2>Writing text to files</h2>
All the example programs that we've seen so far have produced output straight to the screen. That's great for exploring new features and when working on programs, because it allows you to see the effect of changes to the code right away. It has a few drawbacks, however, when writing code that we might want to use in real life.

Printing output to the screen only really works well when there isn't very much of it (Linux users may be aware that we can redirect terminal output to a file using shell redirection, which can get around some of these problems). It's great for short programs and status messages, but quickly becomes cumbersome for large amounts of output. Some terminals struggle with large amounts of text, or worse, have a limited scrollback capability which can cause the first bit of your output to disappear. It's not easy to search in output that's being displayed at the terminal, and long lines tend to get wrapped. Also, for many programs we want to send different bits of output to different files, rather than having it all dumped in the same place.

Most importantly, terminal output vanishes when you close your terminal program. For small programs like the examples in this book, that's not a problem – if you want to see the output again you can just re-run the program. If you have a program that requires a few hours to run, that's not such a great option.

<h3>Opening files for writing</h3>
In the previous section, we saw how to open a file and read its contents. We can also open a file and <i>write</i> some data to it, but we have to use the <code>open</code> function in a slightly different way. To open a file for writing, we use a two-argument version of the <code>open</code> function, where the second argument is a specially-formatted string describing what we want to do to the file (We call this the <i>mode </i>of the file) . This second argument can be "r" for reading, "w" for writing, or "a" for appending (These are the most commonly-used options – there are a few others) . If we leave out the second argument (like we did for all the examples above), Python uses the default, which is "r" for reading.

The difference between "w" and "a" is subtle, but important. If we open a file that already exists using the mode "w", then we will overwrite the current contents with whatever data we write to it. If we open an existing file with the mode "a", it will add new data onto the end of the file, but will <b>not</b> remove any existing content. If there doesn't already exist a file with the specified name, then "w" and "a" behave identically – they will both create a new file to hold the output.

Quite a lot of Python functions and methods have these optional arguments. For the purposes of this tutorial, we will only mention them when they are directly relevant to what we're doing. If you want to see all the optional arguments for a particular method or function, the best place to look is the official Python documentation.

Once we've opened a file for writing, we can use the file <code>write</code> method to write some text to it. <code>write</code> works a lot like <code>print</code> – it takes a single string argument - but instead of printing the string to the screen it writes it to the file.

Here's how we use <code>open</code> with a second argument to open a file and write a single line of text to it:


    my_file = open("out.txt", "w")
    my_file.write("Hello world")


Because the output is being written to the file in this example, you won't see any output on the screen if you run it. To check that the code has worked, you'll have to run it, then open up the file <i>out.txt</i> in your text editor and check that its contents are what you expect (.txt is the standard file name extension for a plain text file. Later when we generate output files with a particular format, we'll use different file name extensions.) .

Remember that with <code>write</code>, just like with <code>print</code>, we can use <b>any</b> string as the argument. This also means that we can use any method or function that <b>returns</b> a string. The following are all perfectly OK:


    # write "abcdef"
    my_file.write("abc" + "def")
    # write "8"
    my_file.write(str(len('AGTGCTAG')))
    # write "TTGC"
    my_file.write("ATGC".replace('A', 'T'))
    # write "atgc"
    my_file.write("ATGC".lower())
    # write contents of my_variable
    my_file.write(my_variable)


<h2>Closing files</h2>
There's one more important file method to look at before we finish this chapter – <code>close</code>. Unsurprisingly, this is the opposite of <code>open</code> (but note that it's a <i>method</i>, whereas <code>open</code> is a <i>function</i>). We should call <code>close</code> after we're done reading or writing to a file – we won't go into the details here, but it's a good habit to get into as it avoids some types of bugs that can be tricky to track down. <code>close</code> is an unusual method as it takes no arguments (so it's called with an empty pair of parentheses) and doesn't return any useful value:


    my_file = open("out.txt", "w")
    my_file.write("Hello world")
    # remember to close the file
    my_file.close()

<h2>Paths and folders</h2>
So far, we have only dealt with opening files in the same folder that we are running our program. What if we want to open a file from a different part of the file system?

The <code>open</code> function is quite happy to deal with files from anywhere on your computer, as long as you give the full path (i.e. the sequence of folder names that tells you the location of the file). Just give a <i>file path</i> as the argument rather than a <i>file name</i>. The format of the file path looks different depending on your operating system. If you're on Linux, it will look like this:


    my_file = open("/home/martin/myfolder/myfile.txt")


if you're on Windows, like this (The extra r character before the string is necessary to prevent Python from trying to interpret the backslash in the file path) :


    my_file = open(r"c:\windows\Desktop\myfolder\myfile.txt")

and if you're on a Mac, like this:

    my_file = open("/Users/martin/Desktop/myfolder/myfile.txt")


<h2>Exercises</h2>
<h2>Splitting genomic DNA</h2>
Look in the <i>data/martin_python</i> folder for a file called <i>genomic_dna.txt </i>– it contains a piece of genomic DNA which comprises two exons and an intron. The first exon runs from the start of the sequence to the sixty-third character, and the second exon runs from the ninety-first character to the end of the sequence. Write a program that will split the genomic DNA into coding and non-coding parts, and write these sequences to two separate files.

<h2>Writing a FASTA file</h2>
FASTA file format is a commonly-used DNA and protein sequence file format. A single sequence in FASTA format looks like this:


    >sequence_name
    ATCGACTGATCGATCGTACGAT


Where sequence_name is a header that describes the sequence (the greater-than symbol indicates the start of the header line). Often, the header contains an accession number that relates to the record for the sequence in a public sequence database. A single FASTA file can contain multiple sequences, like this:


    >sequence_one
    ATCGATCGATCGATCGAT
    >sequence_two
    ACTAGCTAGCTAGCATCG
    >sequence_three
    ACTGCATCGATCGTACCT


Write a program that will create a FASTA file for the following three sequences – make sure that all sequences are in upper case and only contain the bases A, T, G and C.

<table width="556" cellspacing="0" cellpadding="4"><colgroup> <col width="165" /> <col width="373" /></colgroup>
<thead>
<tr valign="TOP">
<th width="165">
<p align="CENTER">Sequence header</p>
</th>
<th width="373">
<p align="CENTER">DNA sequence</p>
</th>
</tr>
</thead>
<tbody>
<tr valign="TOP">
<td width="165">
<p align="CENTER"><code>ABC123</code></p>
</td>
<td width="373">
<p align="CENTER"><code>ATCGTACGATCGATCGATCGCTAGACGTATCG</code></p>
</td>
</tr>
<tr valign="TOP">
<td width="165">
<p align="CENTER"><code>DEF456</code></p>
</td>
<td width="373">
<p align="CENTER"><code>actgatcgacgatcgatcgatcacgact</code></p>
</td>
</tr>
<tr valign="TOP">
<td width="165">
<p align="CENTER"><code>HIJ789</code></p>
</td>
<td width="373">
<p align="CENTER"><code>ACTGAC-ACTGT--ACTGTA----CATGTG</code></p>
</td>
</tr>
</tbody>
</table>

<h2>Writing multiple FASTA files</h2>
Use the data from the previous exercise, but instead of creating a single FASTA file, create three new FASTA files – one per sequence. The names of the FASTA files should be the same as the sequence header names, with the extension <i>.fasta</i>.

