<h2>Defining functions</h2>
Here's a bit of code that we want to turn into a function. This calculates the AT content of a sequence:


    from __future__ import division
    my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
    length = len(my_dna)
    a_count = my_dna.count('A')
    t_count = my_dna.count('T')
    at_content = (a_count + t_count) / length
    print("AT content is " + str(at_content))


Creating our own function to carry out a particular job has many benefits. It allows us to re-use the same code many times within a program without having to copy it out each time. Additionally, if we find that we have to make a change to the code, we only have to do it in one place. Splitting our code into functions also allows us to tackle larger problems, as we can work on different bits of the code independently. We can also re-use code across multiple programs.

<h2>Defining a function</h2>

Let's go ahead and create our <code>get_at_content</code> function. Before we start typing, we need to figure out what the inputs (the number and types of the <i>function arguments</i>) and outputs (the type of the <i>return value</i>) are going to be. For this function, that seems pretty obvious – the input is going to be a single DNA sequence, and the output is going to be a decimal number. To translate these into Python terms: the function will take a single argument of type <i>string</i>, and will return a value of type <i>number</i>. Here's the code:

    def get_at_content(dna):
        length = len(dna)
        a_count = dna.count('A')
        t_count = dna.count('T')
        at_content = (a_count + t_count) / length
        return at_content

<b>Reminder</b>: if you're using Python 2 rather than Python 3, include this line at the top of your program:


    from __future__ import division


The first line of the function definition contains a several different elements. We start with the word <code>def</code>, which is short for <i>define</i> (writing a function is called <i>defining</i> it). Following that we write the name of the function, followed by the names of the argument variables in parentheses. Just like we saw before with normal variables, the function name and the argument names are arbitrary – we can use whatever we like.

The first line ends with a colon, just like the first line of the loops that we were looking at in the previous section. And just like loops, this line is followed by a <i>block</i> of indented lines – the <i>function body</i>. The function body can have as many lines of code as we like, as long as they all have the same indentation. Within the function body, we can refer to the arguments by using the variable names from the first line. In this case, the variable <code>dna</code> refers to the sequence that was passed in as the argument to the function.

The last line of the function causes it to return the AT content that was calculated in the function body. To <code>return</code> from a function, we simply write return followed by the value that the function should output.

There are a couple of important things to be aware of when writing functions. Firstly, we need to make a clear distinction between <i>defining</i> a function, and <i>running</i> it (we refer to running a function as <i>calling</i> it). The code we've written above will not cause anything to happen when we run it, because we've not actually asked Python to execute the <code>get_at_content</code> function – we have simply defined what it is. The code in the function will not be executed until we call the function like this:

    get_at_content("ATGACTGGACCA")

If we simply call the function like that, however, then the AT content will vanish once it's been calculated. In order to use the function to do something useful, we must either store the result in a variable:

    at_content = get_at_content("ATGACTGGACCA")

Or use it directly:

    print("AT content is " + str(get_at_content("ATGACTGGACCA")))

Secondly, it's important to understand that the argument variable <code>dna</code> does not hold any particular value when the function is defined (Indeed, it doesn't actually exist when it's defined, only when it runs). Instead, its job is to hold whatever value is given as the argument when the function is called. 

Finally, be aware that any variables that we create as part of the function only exist inside the function, and cannot be accessed outside. If we try to use a variable that's created inside the function from outside:

    def get_at_content(dna):
        length = len(dna)
        a_count = dna.count('A')
        t_count = dna.count('T')
        at_content = (a_count + t_count) / length
        return at_content
    
    print(a_count)

We'll get an error:

    NameError: name 'a_count' is not defined

<h2>Calling and improving our function</h2>
Let's write a small program that uses our new function, to see how it works. We'll try both storing the result in a variable before printing it (lines 8 and 9) and printing it directly (lines 10 and 11):

    def get_at_content(dna):
        length = len(dna)
        a_count = dna.count('A')
        t_count = dna.count('T')
        at_content = (a_count + t_count) / length
        return at_content
    
    my_at_content = get_at_content("ATGCGCGATCGATCGAATCG")
    print(str(my_at_content))
    print(get_at_content("ATGCATGCAACTGTAGC"))
    print(get_at_content("aactgtagctagctagcagcgta"))

Looking at the output, we can see that the first function call works fine – the AT content is calculated to be 0.45, is stored in the variable <code>my_at_content</code>, then printed. However, the output for the next two calls is not so great. The call at line 10 produces a number with way too many figures after the decimal point, and the call at line 11, with the input sequence in lower case, gives a result of 0.0, which is definitely not correct:

    0.45
    0.5294117647058824
    0.0

We'll fix these problems by making a couple of changes to the <code>get_at_content</code> function. We can add a rounding step in order to limit the number of significant figures in the result. Python has a built-in <code>round</code> function that takes two arguments – the number we want to round, and the number of significant figures. We'll call the <code>round</code> function on the result before we return it. And we can fix the lower case problem by converting the input sequence to upper case before starting the calculation. Here's the new version of the function, with the same three function calls:

    def get_at_content(dna):
        length = len(dna)
        a_count = dna.upper().count('A')
        t_count = dna.upper().count('T')
        at_content = (a_count + t_count) / length
        return round(at_content, 2)
    
    my_at_content = get_at_content("ATGCGCGATCGATCGAATCG")
    print(str(my_at_content))
    print(get_at_content("ATGCATGCAACTGTAGC"))
    print(get_at_content("aactgtagctagctagcagcgta"))

and now the output is just as we want:
    
    0.45
    0.53
    0.52

We can make the function even better though: why not allow it to be called with the number of significant figures as an argument? In the above code, we've picked two significant figures, but there might be situations where we want to see more. Adding the second argument is easy; we just add it to the argument variable list on the first line of the function definition, and then use the new argument variable in the call to <code>round</code>. We'll throw in a few calls to the new version of the function with different arguments to check that it works:

    def get_at_content(dna, sig_figs):
        length = len(dna)
        a_count = dna.upper().count('A')
        t_count = dna.upper().count('T')
        at_content = (a_count + t_count) / length
        return round(at_content, sig_figs)
    
    test_dna = "ATGCATGCAACTGTAGC"
    print(get_at_content(test_dna, 1))
    print(get_at_content(test_dna, 2))
    print(get_at_content(test_dna, 3))

The output confirms that the rounding works as intended:

    0.5
    0.53
    0.529


<h2>Encapsulation with functions</h2>

Let's pause for a moment and consider what happened in the previous section. We wrote a function, and then wrote some code that used that function. In the process of writing the code that used the function, we discovered a couple of problems with our original function definition. <b>We were then able to go back and change the function definition, without having to make any changes to the code that used the function</b>.

I've written that last sentence in bold, because it's incredibly important. It's no exaggeration to say that understanding the implications of that sentence is the key to being able to write larger, useful programs. The reason it's so important is that it describes a programming phenomenon that we call <i>encapsulation</i>. Encapsulation just means dividing up a complex program into little bits which we can work on independently. In the example above, the code is divided into two parts – the part where we define the function, and the part where we use it – and we can make changes to one part without worrying about the effects on the other part.

This is a very powerful idea, because without it, the size of programs we can write is limited to the number of lines of code we can hold in our head at one time. Some of the example code in the solutions to exercises in the previous section were starting to push at this limit already, even for relatively simple problems. By contrast, using functions allows us to build up a complex program from small building blocks, each of which individually is small enough to understand in its entirety.

Because using functions is so important, future solutions to exercises will use them when appropriate, even when it's not explicitly mentioned in the problem text. I encourage you to get into the habit of using functions in your solutions too.

<h2>Functions don't always have to take an argument</h2>

There's nothing in the rules of Python to say that your function <b>must</b> take an argument. It's perfectly possible to define a function with no arguments:

    def get_a_number():
        return 42

but such functions tend not to be very useful. For example, we can write a version of <code>get_at_content</code> that doesn't require any arguments by setting the value of the <code>dna</code> variable inside the function:

    def get_at_content():
        dna = "ACTGATGCTAGCTA"
        length = len(dna)
        a_count = dna.upper().count('A')
        t_count = dna.upper().count('T')
        at_content = (a_count + t_count) / length
        return round(at_content, 2)

but this version will always calculate the same value, unless we change the DNA sequence directly in the code . Occasionally you may be tempted to write a no-argument function that works like this:

    def get_at_content():
        length = len(dna)
        a_count = dna.upper().count('A')
        t_count = dna.upper().count('T')
        at_content = (a_count + t_count) / length
        return round(at_content, 2)
    
    dna = "ACTGATCGATCG"
    print(get_at_content())

At first this seems like a good idea – it works because the function gets the value of the <code>dna</code> variable that is set on line 8 ((It doesn't matter that the variable is set <i>after</i> the function is defined – all that matters it that it's set <i>before</i> the function is called on line 9.)) . However, this breaks the encapsulation that we worked so hard to achieve. The function now only works if there is a variable called <code>dna</code> set in the bit of the code where the function is called, so the two pieces of code are no longer independent.

If you find yourself writing code like this, it's usually a good idea to identify which variables from outside the function are being used inside it, and turn them into arguments.

<h2>Functions don't always have to return a value</h2>
Consider this variation of our function – instead of <i>returning</i> the AT content, this function <i>prints</i> it to the screen:

    def print_at_content(dna):
        length = len(dna)
        a_count = dna.upper().count('A')
        t_count = dna.upper().count('T')
        at_content = (a_count + t_count) / length
        print(str(round(at_content, 2)))

When you first start writing functions, it's very tempting to do this kind of thing. You think "<i>OK, I need to calculate and print the AT content – I'll write a function that does both</i>". The trouble with this approach is that it results in a function that is less flexible. Right now you want to print the AT content to the screen, but what if you later discover that you want to write it to a file, or use it as part of some other calculation? You'll have to write more functions to carry out these tasks.

The key to designing flexible functions is to recognize that the job <i>calculate and print the AT content</i> is actually two separate jobs – calculating the AT content, and printing it. Try to write your functions in such a way that they just do one job. You can then easily write code to carry out more complicated jobs by using your simple functions as building blocks.

<h2>Functions can be called with named arguments</h2>

What do we need to know about a function in order to be able to use it? We need to know what the return value and type is, and we need to know the number and type of the arguments. For the examples we've seen so far in this book, we also need to know the <b>order</b> of the arguments. For instance, to use the <code>open</code> function we need to know that the name of the file comes first, followed by the mode of the file. And to use our two-argument version of <code>get_at_content</code> as described above, we need to know that the DNA sequence comes first, followed by the number of significant figures.

There's a feature in Python called <i>keyword</i><i> arguments </i>which allows us to call functions in a slightly different way. Instead of giving a list of arguments in parentheses:

    get_at_content("ATCGTGACTCG", 2)

we can supply a list of argument variable names and values joined by equals signs:

    get_at_content(dna="ATCGTGACTCG", sig_figs=2)

This style of calling functions (It works with methods too, including all the ones we've seen so far) has several advantages. It doesn't rely on the order of arguments, so we can use whichever order we prefer. These two statements behave identically:

    get_at_content(dna="ATCGTGACTCG", sig_figs=2)
    get_at_content(sig_figs=2, dna="ATCGTGACTCG")

It's also clearer to read what's happening when the argument names are given explicitly.

We can even mix and match the two styles of calling – the following are all identical:

    get_at_content("ATCGTGACTCG", 2)
    get_at_content(dna="ATCGTGACTCG", sig_figs=2)
    get_at_content("ATCGTGACTCG", sig_figs=2)

Although we're not allowed to start off with keyword arguments then switch back to normal – this will cause an error:

    get_at_content(dna="ATCGTGACTCG", 2)

Keyword arguments can be particularly useful for functions and methods that have a lot of arguments.

<h2>Function arguments can have defaults</h2>

We've encountered function arguments with defaults before, when we were discussing opening files. Recall that the <code>open</code> function takes two arguments – a file name and a mode string – but that if we call it with <b>just</b> a file name it uses a default value for the mode string. We can easily take advantage of this feature in our own functions – we simply specify the default value in the first line of the function definition. Here's a version of our <code>get_at_content </code>function where the default number of significant figures is two:

    def get_at_content(dna, sig_figs=2):
        length = len(dna)
        a_count = dna.upper().count('A')
        t_count = dna.upper().count('T')
        at_content = (a_count + t_count) / length
        return round(at_content, sig_figs)

Now we have the best of both worlds. If the function is called with two arguments, it will use the number of significant figures specified; if it's called with one argument, it will use the default value of two significant figures. Let's see some examples:

    get_at_content("ATCGTGACTCG")
    get_at_content("ATCGTGACTCG", 3)
    get_at_content("ATCGTGACTCG", sig_figs=4)

The function takes care of filling in the default value for <code>sig_figs</code> for the first function call where none is supplied:
    
    0.45
    0.455
    0.4545

Function argument defaults allow us to write very flexible functions which can have varying numbers of arguments. It only makes sense to use them for arguments where a sensible default can be chosen – there's no point specifying a default for the <code>dna</code> argument in our example. They are particularly useful for functions where some of the options are only going to be used infrequently.



<h2>Exercises</h2>

<h3>Percentage of amino acid residues, part one</h3>
Write a function that takes two arguments – a protein sequence and an amino acid residue code – and returns the percentage of the protein that the amino acid makes up. Use the following calls to test your function:

my_function("MSRSLLLRFLLFLLLLPPLP", "M")
my_function("MSRSLLLRFLLFLLLLPPLP", "r")
my_function("MSRSLLLRFLLFLLLLPPLP", "L")
my_function("MSRSLLLRFLLFLLLLPPLP", "Y")

<b>Reminder</b>: if you're using Python 2 rather than Python 3, include this line at the top of your program:

    from __future__ import division


<h3>Percentage of amino acid residues, part two</h3>
Modify the function from part one so that it accepts a list of amino acid residues rather than a single one. If no list is given, the function should return the percentage of hydrophobic amino acid residues (A, I, L, M, F, W, Y and V). Test your function with these calls:


my_function("MSRSLLLRFLLFLLLLPPLP", ["M"])
my_function("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) 
my_function("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) 
my_function("MSRSLLLRFLLFLLLLPPLP") 

