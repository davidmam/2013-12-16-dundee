# Shell - crib sheet

* Even in a windows, Windows, world useful to know.
* HPC resources and cloud platform- and infrastructure-as-a-service.
* More than just file and directory management.
* Bolt together programs into powerful data processing pipelines.
* Automation.
* Bash, "Bourne again shell"

## Help

    $ man COMMAND

Up and down arrows to scroll.

`/` followed by search term (e.g. `/help`) then ENTER.

`q` to exit.

    $ COMMAND --help # Command syntax, usage and other information.

Top tip: if writing your own executables, be consistent, and provide `--help`.

## Comments

    # This is a comment. It is not executed.

## Who

    $ who # who is logged on
    $ whoami # who am I logged on as

## Directories

    $ pwd       # Path to current directory (folder in Windows)
    $ ls        # List directory
    $ ls *.txt  # Wild-card
    $ ls *_hai*
    $ ls -R     # Recurse
    $ ls -F     # Append / to directories
    $ ls -l     # Permissions, date, size, owner, group...
    $ ls -t		# list ordered by last modification time
    $ ls -S		# list ordered by size
    $ ls -r		# reverse listing
    $ ls -ltr	# combine different options (long, by time, reversed)
    $ cd /      # Root directory
    $ cd ~      # Home directory. There's no place like ~
    $ ls -a     # Hidden files
    $ ls .      # Current directory
    $ ls ..     # Parent directory
    $ cd ..
    $ cd        # Default to home directory
    $ mkdir directory
    $ mkdir ~/directory
    $ mv directory another_directory
    $ rmdir empty_directory

# Files

    $ cat file           # View file
    $ less file          # Page through file
    $ more file          # Page through file
    $ head -2 file       # First N lines
    $ tail -3 file       # Last N lines
    $ cp file1 file2     # Copy
    $ cp *.txt directory
    $ rm file.txt        # Delete - no recycle bin.
    $ rm -r directory    # Recurse
    $ rm -rf directory   # Recurse and force - beware

## History

Up arrow browses previous commands

    $ history
    $ !NNNN   # Rerun Nth command in history

## Word count

    $ wc file     # Filter
    $ wc -l file  # Lines only
    $ wc -w file  # Words only
    $ wc -l *.txt # Total

Use to find out number of records in a data file if one record per line.

## Regular expressions

    $ ls *.txt        # Zero or more characters
    $ ls ?o*          # Exactly one character
    $ ls a[bcde]*.txt # Exactly one of the characters listed
    $ ls a[cde]*.txt  
    $ ls *.*
    $  *.[!txt]*      # No sequence involving t, x or t

## Searching within files

Global/regular expression/print

    $ grep the haiku.txt
    $ grep day haiku.txt
    $ grep is haiku.txt
    $ grep 'it is' haiku.txt
    $ grep -w is haiku.txt   # Exact match
    $ grep -n it haiku.txt   # lines with matches
    $ grep -i the haiku.txt  # Ignore case
    $ grep -wn is haiku.txt
    $ grep -wnv is haiku.txt # Non-matching lines
    $ grep  -wnr Today *     # Recurse

## Input and output redirection

`>` redirects output (AKA standard output)

    $ grep -r not * > found_nots.txt
    $ cat found_nots.txt
    $ ls *.txt > txt_files.txt
    $ cat txt_files.txt
    $ cat                            # Echoes standard input
    Blah
    CTRL-D
    $ cat > myscript.txt
    Blah
    CTRL-D
    $ cat myscript.txt

`<` redirects input (AKA standard input).

    $ cat < haiku.txt
    $ ls idontexist.txt > output.txt
    $ cat output.txt

Error message is output on standard error.

    $ ls idontexist.txt 2> output.txt               # 2 is standard error
    $ ls haiku.txt 1> output.txt                    # 1 is standard output
    $ ls idontexist.txt haiku.txt > output.txt 2>&1

## Exercise - grep

`pdb/` contains a set of protein database files

Each `.pdb` file lists atoms in a protein

Write a single command that

* Uses `grep` to find all  alpha carbons (`CA`) atoms in all `.pdb` files.
* Stores these in `carbons.txt`.

You will need wild card, exact matches output redirection

Problems with the solution?

 * Chains could be labelled with identifiers `H` and `L` (for heavy and light).
 * `AUTHOR` contains an initial e.g. `HARRY H CORBETT`.

Important:

 * Understand data.
 * Review script.
 * Validate that actual results equal expected results.

## Searching for files

    $ find .                # Find all
    $ find . -type d        # Directories only
    $ find . -type f        # Files only
    $ find . -maxdepth 2    # Maximum depth of tree
    $ find . -mindepth 3    # Minimum depth of tree
    $ find . -name *.txt    # Fails as wild-card is expanded
    $ find . -name '*.txt'  # Name or pattern matching
    $ find . -iname '*.TXT' # Ignore case
    $ find . -empty         # Empty files only
    $ touch emptyfile.txt   # Create empty file
    $ find . -empty

`` back-ticks execute a command

    $ wc -l `find . -name '*.txt'`

## Exercise - find

Write a single command that

* Uses `find` to find all `.pdb` files.
* Uses `cat` to list their contents.
* Stores contents in `proteins.txt`.

You will need back ticks, find file name option, output redirection.

## Power of the pipe

Count text files

    $ find . -name '*.txt' > files.tmp
    $ wc -l files.tmp

`find` outputs a list of files, `wc` inputs a list of files, skip the temporary file.

    $ find . -name '*.txt' | wc -l

`|` is a pipe.

    $ echo "Number of .txt files:" ; find . -name '*.txt' | wc -l

`;` equivalent to running two commands on separate lines.

Question: what does this do?

    $ ls | grep s | wc -l

Answer: counts the number of files with `s` in their name.

    $ history | grep 'wget'

Power of well-defined modular components with well-defined interfaces,

 * Bolt together to create powerful computational and data processing workflows.
 * Good design principle applicable to programming - Python modules, C libraries, Java classes - modularity and reuse.
 * "little pieces loosely joined" - `history` + `grep` = function to search for a command.

## Exercise - pipes

Write a single command that

* Uses `find` to find all `.pdb` files.
* Uses `cat` to list their contents.
* Uses `grep` to find all the hydrogen (`H`) atoms in their contents.
* Uses `wc` to count the number of hydrogen atoms found.
* Stores the count in `hydrogen_count.txt`.

You will need commands from previous exercises, back ticks, pipe.

## Some more tools
###	cut

*cut* allows part of a line to be selected. It will chop out a defined portion of the line, either between certain character positions or by splitting the line based on a specific character. As PDB records are based on a fixed width it is relatively easy to select the portion of the line we want to select. Suppose we want to extract the x coordinate for the atoms. This is in columns 32-38 of each record. We also want the residue name and number (columns 17-25). Using essentially the same command as before to select the ATOM lines, we can then cut out the bits we want.

    % grep ATOM 1boy.pdb | grep -v ATOMS | grep -v ' ATOM' | cut -c 17-25,32-38

(output not shown)

One disadvantage of *cut* is that it just cuts.. it doesn't allow one to change the output, merely select it. The next tool is far more powerful.

### awk

Awk is a tool that manipulates records. It assumes that every text file is some sort of structured document containing records that are divided into fields. Each record is separated by a record separator and each field by a field separator. awk allows the individual fields to be manipulated and incorporates a programming language to allow decision making. awk is a complex tool and you are strongly advised to refer to the book 'sed & awk' from O'Reilly press.
By default the record separator is a newline and the field separator is whitespace (spaces or tabs). This will allow us to do the same manipulation as we did for cut. When awk separates each record into fields, these fields can be selected as the variables $1, $2 and so on. $0 is the whole record.

    % grep ATOM 1boy.pdb | grep -v ATOMS | grep -v ' ATOM' | awk ' {print $4, $5, $6 }'

(output not shown)

One subtle difference is that cut left multiple spaces between the characters. awk has reduced each space to just one character. This is the effect of putting the commas between the variables in the output. (A variable is a named value, just like using letters to stand for numbers in algebra except that variable names can be any length. You can get the value of a variable by putting the $ in front of the name.) If we try this again without the commas then we lose the spaces.

    % grep ATOM 1boy.pdb | grep -v ATOMS | grep -v ' ATOM' | awk ' {print $4 $5 $6} '

(output not shown)

We can also add extra text into each field as desired by including that text between quotes in the print statement.

    % grep ATOM 1boy.pdb | grep -v ATOMS | grep -v ' ATOM' | awk ' {print $4 ,$5,"X:", $6 }'

(output not shown)

awk also allows commands to be run at the beginning and at the end of the report. The commands inside the  are run for every line. To run commands at the beginning we place them inside another set of braces prefixed by the key word BEGIN. Lets add a title to the report and change it a little by only selecting threoning residues.

    % grep ATOM 1boy.pdb | grep -v ATOMS | grep -v ' ATOM' | grep THR | awk ' BEGIN{ print "Threonine residues" }{ print $4, $5}'

(output not shown)

This has printed every threonine residue. It has done more than that, it has printed the residue name and number for each atom in the threonine residues. To shrink this down to one per residue we can either select just eg. alpha carbons or we can use the unix command uniq. uniq will reduce multiple adjacent lines with the same output to just one line. The lines must be adjacent so we would normally precede uniq with sort but it isn't neccessary in this case as the lines are already sorted.

    % grep ATOM 1boy.pdb | grep -v ATOMS | grep -v ' ATOM' | grep THR | awk ' BEGIN {print "Threonine residues"} { print $4, $5' }| uniq

(output not shown)

Counting these residues by appending wc -l will not give the right number as we have added a header line. We can however get awk to do the counting for us. In this case we will count the total number of atoms present. In the BEGIN block we can set a variable to be a counter and start it at 0. Each time we print a line we can add 1 to the counter variable. At the end we can print a summary line by using an END block that does the same as the BEGIN block but at the end. We can get the value of the counter just by putting the name of the variable.

    % grep ATOM 1boy.pdb | grep -v ATOMS | grep -v ' ATOM' | grep THR | awk ' BEGIN { print "Threonine residues"; counter=0; }{ print $4, $5; counter = counter+1}  END{print "Total:", counter, "atoms"}' | uniq

### sed
Sometimes we will need to make many identical changes at various points
through a file. *sed* looks for lines matching a certain pattern (or between lines matching certain
patterns) and can carry out various operations on them. The one we are interested in is
substitution. One should note that *sed* can read from a file (or stdin) but writes to stdout so
if you want to keep the results then you will need to redirect the output to a file (with *>
filename*).
Let us assume for some reason or other that we have determined that all the methioine
residues in our structure are selenomethionine and we wish to rename them. Try something
like the following:

    % sed -e ' /^ATOM/s/MET/SEL/' 1boy.pdb

(output not shown)

If you were smart and used more or grep to view the output then you will have seen that all
the MET residues were changed to SEL.

#### Example
Try to change all the water atoms (HOH) to WAT. (hint: look at how you are choosing the
lines).

sed can do a lot of other things too. Read the book!

## Variables

    $ set                            # See all variables
    $ MYFILE=data.txt
    $ echo $MYFILE
    $ echo "My file name is $MYFILE"
    $ bash                           # Spawn new shell
    $ echo $MYFILE
    CTRL-D
    $ export MYFILE                  # Export to new shells
    $ bash
    $ echo $MYFILE
    CTRL-D
    $ echo $PATH
    $ export PATH=$PATH:/path/to/bin # Common requirement

    $ let NUM=$NUM+1                 # Simple arithmetic
    $ TEXT_FILES=`ls *.txt`          # Save output in variable
    $ echo TEXT_FILES

`.bashrc` to define variables and other actions to do when logging in e.g.

    export JAVA_HOME=/opt/local/java1.5
    export PATH=$JAVA_HOME/bin:$PATH
    export ANT_HOME=/home/michelj/Software/apache-ant-1.7.0
    export PATH=$ANT_HOME/bin:$PATH

## Conditionals

    $ NUM=1
    $ if [ "$NUM" -eq 1 ]; then echo "Equal"; fi
    $ WORD="hello"
    $ if [ "$WORD" = "hello" ];  then echo "The same"; fi

## Loops

    $ for i in `cat file`; do echo $i; done | sort | uniq

    $ for PDB in `find . -name '*.pdb'`; do
        echo $PDB
     done

## Shell scripts

Save retyping.

    $ nano protein_filter.sh
    #!/bin/bash
    DATE=`date`
    echo "Processing date: $DATE"
    for PDB in `find . -name "*.pdb"`; do
        echo $PDB
    done
    echo "Processing completed!"
    
    $ sh protein_filter.sh
    $ chmod +x protein_filter.sh # Mark as executable
    $ ./protein_filter.sh

## Exercise - shell scripts

Edit `protein_filter.sh` so that it

* Has variables `ATOM` with value `'H'` and `PDB_EXT` with value `'pdb'`.
* For each `.pdb` file it prints the file name and a count of the number of hydrogen atoms in that file.
* Double-quotes are used in the `find` expression as this means shell variables are expanded.

You will need parts of your command from the previous exercise.

Edit protein_filter.sh so that it takes the atom value from the command-line e.g.

    $ ./protein_filter.sh H
    $ ./protein_filter.sh C

`$1` provides access to the first command-line argument.

## Permissions

    $ ls -l # permissions, dates, sizes, owner, group, size in byte, creation/modification date/time, name.

Users, groups, others.

Read, write, execute.

    $ chmod a+r haiku.txt     # Add permission - all read
    $ chmod a-r haiku.txt     # Remove permission - all not read
    $ chmod u+r haiku.txt     # User read
    $ chmod g+w haiku.txt     # Group write
    $ chmod o+x haiku.txt     # Other execute
    $ chmod g+rx haiku.txt    # Group read and execute
    $ chmod go+rx haiku.txt   # Group and other read and execute
    $ chmod ugo=rwx haiku.txt # Set permission
 
## Jobs and processes

    $ ./counter.sh > output.txt
    CTRL^Z                        # Suspend
    $ wc -l output.txt
    $ jobs -l                     # Jobs, job number, process ID
    $ fg JOBNUMBER                # Resume in foreground
    CTRL^Z
    $ bg JOBNUMBER                # Resume in background
    $ wc -l output.txt            # Still working
    $ ./counter.sh > output.txt & # Start in background, job number, process ID
    $ kill PROCESSID                  
    $ jobs
    $ ps                          # Processes
    $ top                         # Resource consumption
    $ bash
    $ nohup ./counter.sh > output.txt & # Continue after log out
    $ nohup allows processes to continue even after the user logs out.
    CTRL-D
    $ wc -l output.txt

# Secure shell

    $ ssh username@boot-camp.software-carpentry.org
    $ ssh username@boot-camp.software-carpentry.org ls # Run remote command
    $ scp file.txt username@boot-camp.software-carpentry.org:
    $ scp username@boot-camp.software-carpentry.org:directory/file.txt . # Relative path
    $ scp -r username@boot-camp.software-carpentry.org:directory copy

# Packaging

    $ zip -r pdb.zip pdb  # Package and compress, recurse
    $ mkdir tmp
    $ cp pdb.zip tmp
    $ cd tmp
    $ unzip pdb.zip
   
    $ tar -cvf pdb.tar pdb # Create, list files, file archive
    $ mkdir tmp
    $ cp pdb.tar tmp
    $ tar -xf pdb.tar
    $ zip pdb.tar

Top tip: If preparing bundles, put your content in a directory then zip or tar up that single directory. It can be annoying if someone unzips or untars a bundle and it spews its contents all over their directory, possibly overwriting their files.

Top tip: If preparing bundles of your software put the version number or a date in the name. If someone asks for advice, you'll know exactly what version they have.

    $ ls -l
    $ gzip pdb.tar
    $ gunzip pdb.tar.gz

    $ ls -l pdb.zip
    $ md5sum pdb.zip

Top tip: when putting packages up for download also put up the file size and MD5 sum so people can check they've not been tampered with.

## Download files via command-line

[Primary Care Trust Prescribing Data - April 2011 onwards](http://data.gov.uk/dataset/primary-care-trust-prescribing-data-april-to-june-2011)

    $  wget http://www.ic.nhs.uk/catalogue/PUB02342/prim-care-trus-pres-data-apr-jun-2011-dat.csv

## script

    $ script
    $ ls -l
    $ CTRL-D
    $ cat typescript

Record commands typed, commands with lots of outputs, trial-and-error when building software. 

Send exact copy of command and error message to support.

Turn into blog or tutorial. 

## Shell power

(Bentley, Knuth, McIlroy 1986) [Programming pearls: a literate program](http://dl.acm.org/citation.cfm?id=5948.315654) Communications of the ACM, 29(6), pp471-483, June 1986. DOI: [10.1145/5948.315654].

Dr. Drang, [More shell, less egg](http://www.leancrew.com/all-this/2011/12/more-shell-less-egg/), December 4th, 2011.

Common words problem: read a text file, identify the N most frequently-occurring words, print out a sorted list of the words with their frequences.

10 plus pages of Pascal ... or ... 1 line of shell 

    $ nano words.sh
    tr -cs A-Za-z '\n' | tr A-Z a-z | sort | uniq -c | sort -rn | sed ${1}q
    $ chmod +x words.sh
    $ nano words.sh < README.md
    $ nano words.sh < README.md 10

"A wise engineering solution would produce, or better, exploit-reusable parts." - Doug McIlroy

##Text modification

### sed
The 'stream editor' works by performing a series of commands in order on each line.

    $ sed -e 's/the/THE/g' < haiku.txt # changes (substitutes) all 'the' to 'THE' (without the g it woudl just change the first)
    $ sed -e '/the/d' <haiku.txt # delete all lines with the three letter pattern 'the' in.
	$ sed -e '/END/,$d' #delete all lines from the first line containing END to the end of the file.    
    
    
e.g. to change the FASTA file headers from >SwissProt:Accession to >Accession you could use:

    $ sed -e '/>/s/SwissProt://' <seqs.fasta >editedseqs.fasta
    
It is a good idea to test this before doing anything by piping to more

	$ sed -e '/>/s/SwissProt//' <seqs.fasta | more
and to limit the output to just the headers (and avoid lots of unneccessary stuff)
	$ sed -e  '/>/s/SwissProt//' <seqs.fasta | grep '>' | more    
    
sed is very powerful and this just scratches the surface of what it can do.

### awk

Awk is a field based processor that is very useful for selecting specific fields and rewriting the file.
If you have (for example) a tab separated data file and want to combine or rearrange columns it makes it very easy.

    $ awk -F "\t" '{print $2, $3, $1, $4}' < infile.tab
You don't have to print every column. E.g. to print the size of every file.
	$ ls -l | awk '{print $9 " ("$5" bytes)"}' 

### join and paste

So you have a set of data in one file and a set of data in another. You want to join them together so the data in file 1 is added to the data in file 2 as a new column.

    $ join file1 file2 > output # join the fields in file 1 with the fields in file 2 where the first field matches
    
There are many options to tweak how join works. 
	$ man join

Alternatively, if your data is structured appropriately you can use paste to put each file into a separate column in the new dataset.

	$ paste file1 file2 file3 file4 > output # creates a file with the lines joined by tab characters.

## Summary

Shell and scripts

* Modular components with specific responsibilities and well-defined APIs.
* Glue together into powerful computational and data processing pipelines.
* Reduce errors by reusing tried-and-tested components.
* Reduce errors by automation - history, shell scripts.
* Don't reinvent the wheel.
* Free up time to do research.

## Links

* [Software Carpentry](http://software-carpentry.org/)'s online [shell](http://software-carpentry.org/4_0/shell/) lectures.
* G. Wilson, D. A. Aruliah, C. T. Brown, N. P. Chue Hong, M. Davis, R. T. Guy, S. H. D. Haddock, K. Huff, I. M. Mitchell, M. Plumbley, B. Waugh, E. P. White, P. Wilson (2012) "[Best Practices for Scientific Computing](http://arxiv.org/abs/1210.0530)", arXiv:1210.0530 [cs.MS].

## Exercises

### grep

    grep -w 'H' *pdb > hydrogen.txt

Check attendees all have same result.

    wc hydrogen.txt

### find

    cat `find . -name '*.pdb'` > proteins.txt

Check via comparing expected to actual result - lookahead to testing.

    wc pdb/*.pdb
    wc proteins.txt

### Pipes

    cat `find . -name '*.pdb'` | grep -w 'H' | wc -l > hydrogen_count.txt

### Shell scripts

    DATE=`date`
    ATOM=$1
    PDB_EXT="pdb"

    echo "Processing date: $DATE"
    for PDB in `find . -name "*.$PDB_EXT"`; do
        COUNT=`grep -w $ATOM $PDB | wc -l`
        echo "$PDB $COUNT"
    done
    echo "Processing completed!"
