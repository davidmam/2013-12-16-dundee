<h2>The importance of patterns in biology</h2>

A lot of what we do when writing programs for biology can be described as searching for <i>patterns</i> in <i>strings</i>. Because these types of problems crop up in so many different fields, there's a standard set of tools in Python (And in many other languages and utilities) for dealing with them: <i>regular expressions.</i> Regular expressions  are a topic that might not be covered in a general-purpose programming book, but because they're so useful in biology, we're going to devote the whole of this tutorial to looking at them.

Although the tools for dealing with regular expressions are built in to Python, they are not made automatically available when you write a program. In order to use them we must first talk about modules.

<h2>Modules in Python</h2>
The functions and data types that we've discussed so far in this book have been ones that are likely to be needed in pretty much every program – tools for dealing with strings and numbers, for reading and writing files, and for manipulating lists of data. As such, they are automatically made available when we start to create a Python program. If we want to open a file, we simply write a statement that uses the <code>open</code> function.

However, there's another category of tools in Python which are more specialized. Regular expressions are one example, but there is a large list of specialized tools which are very useful when you need them, but are not likely to be needed for the majority of programs. Examples include tools for doing advanced mathematical calculations, for downloading data from the web, for running external programs, and for manipulating date/time information. Each collection of specialized tools – really just a collection of specialized <i>functions</i> and data <i>types</i> – is called a <i>module</i>.

For reasons of efficiency, Python doesn't automatically make these modules available in each new program, as it does with the more basic tools. Instead, we have to explicitly load each module of specialized tools that we want to use inside our program. To load a module we use the <code>import</code> statement. For example, the module that deals with regular expressions is called <code>re</code>, so if we want to write a program that uses the regular expression tools we must include the line:


    import re


at the top of our program. When we then want to use one of the tools from a module, we have to prefix it with the module name. For example, to use the regular expression <code>search</code> function (which we'll discuss later in this section) we have to write:


    re.search(pattern, string)

rather than simply:

    search(pattern, string)

If we forget to import the module which we want to use, or forget to include the module name as part of the function call, we will get a <code>NameError</code>.

For the rest of this section, all code examples will require the <code>import re</code> statement in order to work. For clarity, we won't include it, so if you want try running any of the code in this section, you'll need to add it at the top.

<h2>Raw strings</h2>
Writing regular expression patterns requires us to type a lot of special characters. Recall from the introduction that certain combinations of characters are interpreted by Python to have special meaning. For example, <code>\n</code> means <i>start a new line</i>, and <code>\t</code> means <i>insert a tab character</i>.

Unfortunately, there are a limited number of special characters to go round, so some of the characters that have a special meaning in regular expressions clash with the characters that <b>already</b> have a special meaning. Python's way round this problem is to have a special rule for strings: if we put the letter <code>r</code> immediately before the opening quotation mark, then any special characters inside the string are ignored:


    print(r"\t\n")

The r stands for <i>raw</i>, which is Python's description for a string where special characters are ignored. Notice that the <code>r</code> goes <b>outside</b> the quotation marks – it is not part of the string itself. We can see from the output that the above code prints out the string just as we've written it:

    \t\n

without any tabs or new lines. You'll see this special <i>raw</i> notation used in all the regular expression code examples in this section.

<h2>Searching for a pattern in a string</h2>
We'll start off with the simplest regular expression tool. <code>re.search</code> is a true/false function that determines whether or not a pattern appears somewhere in a string. It takes two arguments, both strings. The first argument is the pattern that you want to search for, and the second argument is the string that you want to search in. For example, here's how we test if a DNA sequence contains an EcoRI restriction site:


    dna = "ATCGCGAATTCAC"
    if re.search(r"GAATTC", dna):
        print("restriction site found!")


Notice that we've used the raw notation for the pattern, even though it's not strictly necessary as it doesn't contain any special characters.

<h3>Alternation</h3>
The above example isn't particularly interesting, as the restriction motif has no variation. Let's try it with the AvaII motif, which cuts at two different motifs: GGACC and GGTCC. We can use the techniques we learned in the previous section to make a complex condition using <code>or</code>:


    dna = "ATCGCGAATTCAC"
    if re.search(r"GGACC", dna) or re.search(r"GGTCC", dna):
        print("restriction site found!")


But a better way is to capture the variation in the AvaII site using a regular expression:

    dna = "ATCGCGAATTCAC"
    if re.search(r"GG(A|T)CC", dna):
        print("restriction site found!")

Here we're using the alternation feature of regular expressions. Inside parentheses, we write the alternatives separated by a pipe character, so <code>(A|T)</code> means <i>either A or T</i>. This lets us write a single pattern – <code>GG(A|T)CC</code> – which captures the variation in the motif.

<h3>Character groups</h3>

The BisI restriction enzyme cuts at an even wider range of motifs – the pattern is GCNGC, where N represents any base. We can use the same alternation technique to search for this pattern:

    dna = "ATCGCGAATTCAC"
    if re.search(r"GC(A|T|G|C)GC", dna):
        print("restriction site found!")

However, there's another regular expression feature that lets us write the pattern more concisely. A pair of square brackets with a list of characters inside them can represent any one of these characters. So the pattern <code>GC[ATGC]GC</code> will match <code>GCAGC</code>, <code>GCTGC</code>, <code>GCGGC</code> and <code>GCCGC</code>. Here's the same program using character groups:

    dna = "ATCGCGAATTCAC"
    if re.search(r"GC[ATGC]GC", dna):
        print("restriction site found!")

If we want a character in a pattern to match <b>any </b>character in the input, we can use a period – the pattern <code>GC.GC</code> would match all four possibilities. However, the period would also match any character which is not a DNA base, or even a letter. Therefore, the whole pattern would also match <code>GCFGC</code>, <code>GC&GC</code> and <code>GC9GC</code>, which may not be what we want.

Sometimes it's easier, rather than listing all the acceptable characters, to specify the characters that we <b>don't</b> want to match. Putting a caret ^ at the start of a character group like this [^XYZ] will negate it, and match any character that <b>isn't</b> in the group.

<h3>Quantifiers</h3>
The regular expression features discussed above let us describe variation in the individual characters of patterns. Another group of features, <i>quantifiers</i>, let us describe variation in the number of times a section of a pattern is repeated.

A question mark immediately following a character means that that character is optional – it can match either <b>zero or one</b><b> times</b>. So in the pattern <code>GAT?C </code>the <code>T</code> is optional, and the pattern will match either <code>GATC</code> or <code>GAC</code>. If we want to apply a question mark to more than one character, we can group the characters in parentheses. For example, in the pattern GGG(AAA)?TTT the group of three <code>A</code>s is optional, so the pattern will match either <code>GGGAAATTT</code> or <code>GGGTTT</code>.

A plus sign immediately following a character or group means that the character or group <b>must</b> be present but can be repeated any number of times – in other words, it will match <b>one or more times</b>. For example, the pattern <code>GGGA+TTT</code> will match three <code>G</code>s, followed by one or more <code>A</code>s, followed by three <code>T</code>s. So it will match <code>GGGATTT</code>, <code>GGGAATT</code>, <code>GGGAAATT</code>, etc. but <b>not</b> <code>GGGTTT</code>.

An asterisk immediately following a character or group means that the character or group is optional, but can also be repeated. In other words, it will match <b>zero or more times</b>. For example, the pattern <code>GGGA*TTT</code> will match three <code>G</code>s, followed by zero or more <code>A</code>s, followed by three <code>T</code>s. So it will match <code>GGGTTT</code>, <code>GGGATTT</code>, <code>GGGAATTT</code>, etc.

If we want to specify a specific number of repeats, we can use curly brackets. Following a character or group with a <b>single</b> number inside curly brackets will match exactly that number of repeats. For example, the pattern <code>GA{5}T</code> will match <code>GAAAAAT </code>but not <code>GAAAAT</code> or <code>GAAAAAAT</code>. Following a character or group with a <b>pair of numbers</b> inside curly brackets separated with a comma allows us to specify an acceptable range of number of repeats. For example, the pattern <code>GA{2,4}T</code> will match <code>GAAT</code>, <code>GAAAT</code> and <code>GAAAAT</code> but not <code>GAT</code> or <code>GAAAAAT</code>.

<h3>Positions</h3>

The final set of regular expression tools we're going to look at don't represent characters at all, but rather positions in the input string. The caret symbol <code>^</code> matches the <b>start</b> of a string, and the dollar symbol <code>$</code> matches the <b>end</b> of a string. The pattern <code>^AAA </code>will match <code>AAATTT</code> but not <code>GGGAAATTT</code>. The pattern <code>GGG$</code> will match <code>AAAGGG</code> but not <code>AAAGGGCCC</code>.
<h3>Combining</h3>

The real power of regular expressions comes from combining these tools. We can use quantifiers together with alternations and character groups to specify very flexible patterns. For example, here's a complex pattern to identify full-length eukaryotic messenger RNA sequences:

    ^ATG[ATGC]{30,1000}A{5,10}$

Reading the pattern from left to right, it will match:
<ul>
	<li>an ATG start codon at the beginning of the sequence</li>
	<li>followed by between 30 and 1000 bases which can be A, T, G or C</li>
	<li>followed by a poly-A tail of between 5 and 10 bases at the end of the sequence</li>
</ul>
As you can see, regular expressions can be quite tricky to read until you're familiar with them! However, it's well worth investing a bit of time learning to use them, as the same notation is used across multiple different tools. The regular expression skills that you learn in Python are transferable to other programming languages, command line tools, and text editors.

The features we've discussed above are the ones most useful in biology, and are sufficient to tackle all the exercises at the end of the section. However, there are many more regular expression features available in Python. If you want to become a regular expression master, it's worth reading up on <i>greedy vs. minimal quantifiers</i>, <i>back-references</i>, <i>lookahead</i> and <i>lookbehind assertions</i>, and<i> built-in character classes</i>.

Before we move on to look at some more sophisticated uses of regular expressions, it's worth noting that there's a method similar to <code>re.search</code> called <code>re.match</code>. The difference is that <code>re.search</code> will identify a pattern occurring <b>anywhere</b> in the string, whereas <code>re.match</code> will only identify a pattern if it matches the <b>entire</b> string. Most of the time we want the former behaviour.

<h2>Extracting the part of the string that matched</h2>

In the section above we used <code>re.search</code> as the condition in an <code>if</code> statement to decide whether or not a string contained a pattern. Often in our programs, we want to find out not only <b>if</b> a pattern matched, but <b>what part </b>of the string was matched. To do this, we need to store the result of using <code>re.search</code>, then use the <code>group</code> method on the resulting object.

When introducing the <code>re.search</code> function above I wrote that it was a true/false function. That's not <i>exactly</i> correct though – if it finds a match, it doesn't return <code>True</code>, but rather an object that is evaluated as true in a conditional context (if the distinction doesn't seem important to you, then you can safely ignore it). The value that's actually returned is a match object – a new data type that we've not encountered before. Like a file object (that we learned about in the first sessino), a match object doesn't represent a simple thing, like a number or string. Instead, it represents the results of a regular expression search. And again, just like a file object, a match object has a number of useful methods for getting data out of it.

One such method is the <code>group</code> method. If we call this method on the result of a regular expression search, we get the portion of the input string that matched the pattern:

    dna = "ATGACGTACGTACGACTG"
    # store the match object in the variable m
    m = re.search(r"GA[ATGC]{3}AC", dna)
    print(m.group())

In the above code, we're searching inside a DNA sequence for <code>GA</code>, followed by three bases, followed by <code>AC</code>. By calling the <code>group</code> method on the resulting match object, we can see the part of the DNA sequence that matched, and figure out what the middle three bases were:

    GACGTAC

What if we want to extract more than one bit of the pattern? Say we want to match this pattern:

    GA[ATGC]{3}AC[ATGC]{2}AC

That's <code>GA</code>, followed by three bases, followed by <code>AC</code>, followed by two bases, followed by <code>AC</code> again. We can surround the bits of the pattern that we want to extract with parentheses – this is called <i>capturing</i> it:

    GA([ATGC]{3})AC([ATGC]{2})AC

We can now refer to the captured bits of the pattern by supplying an argument to the <code>group</code> method. <code>group(1)</code> will return the bit of the string matched by the section of the pattern in the first set of parentheses, <code>group(2)</code> will return the bit matched by the second, etc.:

    dna = "ATGACGTACGTACGACTG"
    # store the match object in the variable m
    m = re.search(r"GA([ATGC]{3})AC([ATGC]{2})AC", dna)
    print("entire match: " + m.group())
    print("first bit: " + m.group(1))
    print("second bit: " + m.group(2))

The output shows that the three bases in the first variable section were <code>CGT</code>, and the two bases in the second variable section were <code>GT</code>:

    entire match: GACGTACGTAC
    first bit: CGT
    second bit: GT


<h2>Getting the position of a match</h2>
As well as containing information about the <b>contents</b> of a match, the match object also holds information about the <b>position</b> of the match. The <code>start</code> and <code>end</code> methods get the positions of the start and end of the pattern on the sequence:

    dna = "ATGACGTACGTACGACTG"
    m = re.search(r"GA([ATGC]{3})AC([ATGC]{2})AC", dna)
    print("start: " + str(m.start()))
    print("end: " + str(m.end()))

Remember that we start counting from zero, so in this case, the match starting at the third base has a start position of two:

    start: 2
    end: 13

We can get the start and end positions of individual groups by supplying a number as the argument to <code>start</code> and <code>end</code>:

    dna = "ATGACGTACGTACGACTG"
    m = re.search(r"GA([ATGC]{3})AC([ATGC]{2})AC", dna)
    print("start: " + str(m.start()))
    print("end: " + str(m.end()))
    print("group one start: " + str(m.start(1)))
    print("group one end: " + str(m.end(1)))
    print("group two start: " + str(m.start(2)))
    print("group two end: " + str(m.end(2)))

In this particular case, we could figure out the start and end positions of the individual groups from the start and end positions of the whole pattern:

    start: 2
    end: 13
    group one start: 4
    group one end: 7
    group two start: 9
    group two end: 11

but that might not always be possible for patterns that have variable length repeats.

<h2>Splitting a string using a regular expression</h2>
Occasionally it can be useful to split a string using a regular expression pattern as the delimiter. The normal string <code>split</code> method doesn't allow this, but the <code>re</code> module has a <code>split</code> function of its own that takes a regular expression pattern as an argument. The first argument is the pattern, the second argument is the string to be split.

Imagine we have a consensus DNA sequence that contains ambiguity codes, and we want to extract all runs of contiguous unambiguous bases. We need to split the DNA string wherever we see a base that isn't A, T, G or C:

    dna = "ACTNGCATRGCTACGTYACGATSCGAWTCG"
    runs = re.split(r"[^ATGC]", dna)
    print(runs)

Recall that putting a caret ^ at the start of a character group negates it. The output shows how the function works – the return value is a list of strings:

    ['ACT', 'GCAT', 'GCTACGT', 'ACGAT', 'CGA', 'TCG']

<h2>Finding multiple matches</h2>
The examples we've seen so far deal with cases where we're only interested in a single occurrence of a pattern in a string. If instead we want to find every place where a pattern occurs in a string, there are two functions in the <code>re</code> module to help us.

<code>re.findall</code> returns a list of all matches of a pattern in a string. The first argument is the pattern, and the second argument is the string. Say we want to find all runs of <code>A</code> and <code>T</code> in a DNA sequence longer than five bases:

    dna = "ACTGCATTATATCGTACGAAATTATACGCGCG"
    runs = re.findall(r"[AT]{4,100}", dna)
    print(runs)

Notice that the return value of the <code>findall</code> method is not a match object – it is a straightforward list of strings:

    ['ATTATAT', 'AAATTATA']

so we have no way to extract the positions. If we want to do anything more complicated than simply extracting the text of the matches, we need to use the <code>re.finditer</code> method. <code>finditer</code> returns a sequence of match objects, so to do anything useful with it, we need to use the return value in a loop:

    dna = "ACTGCATTATATCGTACGAAATTATACGCGCG"
    runs = re.finditer(r"[AT]{3,100}", dna)
    for match in runs:
        run_start = match.start()
        run_end = match.end()
        print("AT rich region from " + str(run_start) + " to " + str(run_end))

As we can see from the output:

    AT rich region from 5 to 12
    AT rich region from 18 to 26

<code>finditer</code> gives us considerably more flexibility that <code>findall</code>.

<h2>Exercises</h2>

<h2>Accession names</h2>
Here's a list of made-up gene accession names:

xkn59438, yhdck2, eihd39d9, chdsye847, hedle3455, xjhd53e, 45da, de37dp

Write a program that will print only the accession names that satisfy the following criteria – treat each criterion separately:
<ul>
	<li>contain the number 5</li>
	<li>contain the letter d or e</li>
	<li>contain the letters d and e in that order</li>
	<li>contain the letters d and e in that order with a single letter between them</li>
	<li>contain both the letters d and e in any order</li>
	<li>start with x or y</li>
	<li>start with x or y and end with e</li>
	<li>contain three or more numbers in a row</li>
	<li>end with d followed by either a, r or p</li>
</ul>

Use this piece of code as a template:

	import re
	
	accs = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]
	my_pattern = r'put your regular expression pattern here'
	for acc in accs:
	    if re.search(my_pattern, acc):
	        print(acc)

<h2>Double digest</h2>
In the martin_python folder, there's a file called <i>dna.txt</i> which contains a made-up DNA sequence. Predict the fragment lengths that we will get if we digest the sequence with two made-up restriction enzymes – AbcI, whose recognition site is <code>ANT*AAT</code>, and AbcII, whose recognition site is <code>GCRW*TG</code> (asterisks indicate the position of the cut site).
