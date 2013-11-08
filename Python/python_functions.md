
# Functions and Documentation

## Functions

In the last session you wrote some scripts to extract data from files, and to substitute text in files. The scripts are good, but are not very easy to use or reusable. For someone to make use of the scripts, they will have to edit them and copy and paste your code every time they want to use your work.

Functions provide a way of packaging code into reusable and easy-to-use components. Lets imagine I have some code to add together two arrays

    $ a = [1, 2, 3, 4]
    $ b = [5, 6, 7, 8]
    $ c = []
    $ for i in range(0,len(a)):
    $     c.append( a[i] + b[i] )
    $
    $ c
    [6, 8, 10, 12]

I can turn this into a function by using "def"

    $ def addArrays(x, y):
    $     z = []
    $     for i in range(0,len(x)):
    $         z.append(x[i] + y[i])
    $     return z

I can add the arrays by calling the function

    $ c = addArrays(a,b)
    $ c
    [6, 8, 10, 12]

In this case I have called the function "addArrays" and passed in the arguments "a" and "b". "a" is copied to "x", while "b" is copied to "y". The function addArrays then acts on "x" and "y", creating the summed array "z". It then returns the new array "z", which is copied back to "c".

Here is another example

    $ r = [ 0.1, 0.2, 0.3 ]
    $ s = [ 5, 12, 8 ]
    $ t = addArrays(r, s)
    $ t
    [5.1, 12.2, 8.3]

Note that we can pass the values to the function directly, e.g.

    $ r = addArrays( [ 1, 2, 3], [5, 6, 7] )
    $ r
    [6, 8, 10]

Note that you must pass in the right number of arguments to a function. addArrays expects two arguments, so if you pass more or less, then that is an error.

    $ r = addArrays()
    TypeError: addArrays() takes exactly 2 arguments (0 given)
    $ r = addArrays(a, b, c)
    TypeError: addArrays() takes exactly 2 arguments (3 given)

Note also that you can define your function to take as many arguments, and return as many values as you want, e.g.

    $ def lotsOfArgs(a, b, c, d, e):
    $     return (a+b, c+d, e)
    $
    $ (r, s, t) = lotsOfArgs(1, 2, 3, 4, 5)
    $ r
    3
    $ s
    7
    $ t
    5

## Exercise

### Exercise 3a

In the last session you wrote a python script that substituted all words that followed “the” in the text file with “banana”. Rewrite your script so that the code is put into a function. The function should have a function signature like this;

    def substitute(filename):
        
The first argument is the name of the file in which the text will be replaced. The function should print the substituted text to the screen.

If you get stuck, an example script is [here](python_functions/substitute.py)

### Exercise 3b

Extend your script so that the function has a second argument, e.g.

    def substitute(filename, new_text):

where “new_text” is the string that replaces any word after “the”, e.g.

    substitute(“textfile”, “banana”)

would replace all words after “the” with “banana”, while

    substitute(“textfile”, “teapot”)

would replace all words after “the” with “teapot”.

In addition, instead of printing the substituted text to the script, return the substituted text as an array of strings.

If you get stuck, an example script is [here](python_functions/substitute2.py)

## Modules

Functions are great for organising your software into self-contained, reusable blocks of code. However, as it stands, you have to copy and paste your function into every script or program in which it is used. Modules (also called libraries) provide a way of packaging up a collection of functions into a single, reusable package. In python, creating a module is very easy. Indeed, you have already done it! The python scripts you have written are actually already python modules. You can import all of the functions defined in a script by using the "import" command.

    $ import substitute

    To be, or not to be, that is the banana:
    Whether 'tis Nobler in the banana to suffer
    the banana and Arrows of outrageous Fortune,
    Or to take Arms against a Sea of troubles,
    And by opposing end them: to die, to sleep

The "import" command has loaded the script, importing all functions, and then running all of the code. If we type "quit" we can exit back to the prompt.

Now at the prompt, I have access to all of the functions contained in [substitute.py](substitute.py). These functions are prefixed with the name “substitute, e.g.

    $ substitute.[TAB]
    substitute.line       substitute.py         substitute.re        
    substitute.lines      substitute.pyc        substitute.substitute

I can call the substitute function from the prompt

    $ substitute.substitute(“textfile”, “orange”)

    ['To be, or not to be, that is the orange:\n',
     "Whether 'tis Nobler in the orange to suffer\n",
     'the orange and Arrows of outrageous Fortune,\n',
     'Or to take Arms against a Sea of troubles,\n',
     'And by opposing end them: to die, to sleep\n',

While this is great, it was quite annoying that the actual code in [substitue.py](substitute.py) was run when we imported the function. We can stop this from happening by using a python hidden variable. Hidden
variables begin with one or two underscores, and we can list them all using ipython TAB

    $ _[TAB]
    _                  __IPYTHON__        __doc__            _i                 _ih                
    _2                 __IPYTHON__active  __import__         _i1                _ii                
    _3                 ___                __name__           _i2                _iii               
    _4                 __builtin__        __package__        _i3                _oh                
    __                 __debug__          _dh                _i4                _sh           

We want the one called "__name__"

    $ __name__
    '__main__'

This gives the name of the current function or module. The top level function is called "__main__". To stop the code in our substitute.py script from running, we just need to make sure that it is only run if the value of "__name__" is "__main__". For example, the [checkmain.py](checkmain.py) script does exactly that;

    def addArrays(x, y):
        z = []
        for i in range(0,len(x)):
            z.append( x[i] + y[i] )
    
        return z
    
    
    if __name__ == "__main__":
        # Don't run this code if this script is being
        # imported as a module 
    
        a = [ 1, 2, 3, 4 ]
        b = [ 5, 6, 7, 8 ]
    
        c = addArrays(a, b)
        print( c )

If I run this script from the command line, then the whole script is executed;

    $ python checkmain.py
    [6, 8, 10, 12]

However, if I import the script, then "__name__" is not equal to "__main__", so that part of the script is skipped;

    $ ipython
    $ import checkmain
    $ checkmain.addArrays( [1, 2, 3], [4, 5, 6] )
    [5, 7, 9]

It is extremely good programming practice to write all of your scripts as if they were modules (and indeed to write all of your code as if they were part of a reusable library). This makes it really easy for you to pick up and reuse all of your code, preventing you from having to continually rewrite the same functionality over and over again.

## Exercise

### Exercise 3c

Edit your [substitute.py](substitute.py) script so that it can be re-used as a module. Do this by adding in an 'if __name__ == "__main__":' check.

If you are really stuck, there is an example script [here](python_functions/substitute3.py).

## Documentation

You have now learned how to package code into functions and to package functions into modules (also called libraries). Functions and modules let you easily design, write and package your code so that it is easy to understand and easily reusable. However, to share the code, and really understand what it works, you need to add documentation.

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

Lets compare this to the documentation for the "checkmain.py" script.

    $ import checkmain
    $ help(checkmain)
    
    Help on module checkmain:

    NAME
        checkmain

    FILE
        /Users/chris/Work/Teaching/swcarpentry/exeter/2013-11-14-exeter/Python/checkmain.py

    FUNCTIONS
        addArrays(x, y)

Not great... It is very important when programming in any language that we provide full documentation for all of the functions and modules. In python, this is achieved by adding documentation strings to each part of the script. These are strings that are placed at the beginning of the function or module.

    $ def documentedFunction(a):
    $     """Here is the documentation string for this function"""
    $     return a
    $
    $ help(documentedFunction)
    
    Help on function documentedFunction in module __main__:
    
    documentedFunction(a)
        Here is the documentation string for this function

We can do the same thing for the [checkmain.py](checkmain.py) script;

    """checkmain is a simple python script to demonstrate
       hiding the code if the script is imported as a module"""

    def addArrays(x, y):
        """This function adds together each element of the two
           passed lists, returning the result in the returned list."""
        z = []
        for i in range(0,len(x)):
            z.append( x[i] + y[i] )
    
        return z
    
    
    if __name__ == "__main__":
        # Don't run this code if this script is being
        # imported as a module 
    
        a = [ 1, 2, 3, 4 ]
        b = [ 5, 6, 7, 8 ]
    
        c = addArrays(a, b)
        print( c )

We now get better documentation when using help()

    $ ipython
    $ import checkmain
    $ help(checkmain)
    Help on module checkmain:
    
    NAME
        checkmain
    
    FILE
        /Users/chris/Work/Teaching/swcarpentry/exeter/2013-11-14-exeter/Python/checkmain.py
    
    DESCRIPTION
        checkmain is a simple python script to demonstrate
        hiding the code if the script is imported as a module
    
    FUNCTIONS
        addArrays(x, y)
            This function adds together each element of the two
            passed lists, returning the result in the returned list.

## Exercise

### Exercise 3d

Edit your [substitute.py](substitute.py) script and add documentation strings for the module and also for all of the functions.

If you are really stuck then there is an example script [here](python_functions/substitute4.py)
