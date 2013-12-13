## Documentation

<h2> Use comments to annotate your code</h2>
Occasionally, we want to write some text in a program that is for humans to read, rather than for the computer to execute. We call this type of line a <i>comment</i>. To include a comment in your source code, start the line with a hash symbol:


	# this is a comment, it will be ignored by the computer
	print("Comments are very useful!")

Comments are a very useful way to document your code, for a number of reasons:
<ul>
	<li>You can put the explanation of what a particular bit of code does right next to the code itself. This makes it much easier to find the documentation for a line of code that is in the middle of a large program, without having to search through a separate document.</li>
	<li>  Because the comments are part of the source code, they can never get mixed up or separated. In other words, if you are looking at the source code for a particular program, then you automatically have the documentation as well. In contrast, if you keep the documentation in a separate file, it can easily become separated from the code.</li>
	<li>Having the comments right next to the code acts as a reminder to update the documentation whenever you change the code. The only thing worse than undocumented code is code with old documentation that is no longer accurate!</li>
</ul>
Don't make the mistake, by the way, of thinking that comments are only useful if you are planning on showing your code to somebody else. When you start writing your own code, you will be amazed at how quickly you forget the purpose of a particular section or statement. If you are working on a solution to one of the exercises in this book on Friday afternoon, then come back to it on Monday morning, it will probably take you quite a while to pick up where you left off.

Comments can help with this problem by giving you hints about the purpose of code, meaning that you spend less time trying to understand your old code, thus speeding up your progress. A side benefit is that writing a comment for a bit of code reinforces your understanding at the time you are doing it. A good habit to get into is writing a quick one-line comment above any line of code that does something interesting:


	# print a friendly greeting
	print("Hello world")

## docstrings

You have already seen documentation using python "help()". For example, lets look at the documentation for the “re” module that we have been using for regular expressions.

    $ ipython
    $ import re
    $ help(re)

    Help on module re:

    NAME
        re - Support for regular expressions (RE).

    FILE
        /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/re.py

    MODULE DOCS
        http://docs.python.org/library/re

    DESCRIPTION
        This module provides regular expression matching operations similar to
        those found in Perl.  It supports both 8-bit and Unicode strings; both
        the pattern and the strings being processed can contain null bytes and
        characters outside the US ASCII range.

However, if we ask for the help for one of our functions:
	
	help(get_at_content)
	Help on function get_at_content in module __main__:
	get_at_content(dna)


Not great... It is very important when programming in any language that we provide full documentation for all of the functions and modules. In python, this is achieved by adding documentation strings to each part of the script. These are strings that are placed at the beginning of the function or module.

    $ def documentedFunction(a):
    $     """Here is the documentation string for this function"""
    $     return a
    $
    $ help(documentedFunction)
    
    Help on function documentedFunction in module __main__:
    
    documentedFunction(a)
        Here is the documentation string for this function

We can do the same thing for our get_at_content function;

    def get_at_content(dna):
      """returns the AT content of a DNA string. The string must be in upper case"""
      length = len(dna)
      a_count = dna.count('A')
      t_count = dna.count('T')
      at_content = (a_count + t_count) / length
      return at_content

We now get better documentation when using help()
  
	help(get_at_content)
	Help on function get_at_content in module __main__:
	get_at_content(dna)
	returns the AT content of a DNA string. The string must be in upper case


##Exercise

Go back through the code and functions that you have written for previous exercises and add comments (and docstrings where appropriate) to explain how the code works. These will help you to remember what you learned when you come back to look at your code in the future.  
    
     
