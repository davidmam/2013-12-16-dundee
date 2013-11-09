# Testing

Testing is extremely important. Without testing, you cannot be sure that your code is doing what you think.
Testing is an integral part of software development, and should be done *while* you are writing code, not 
after the code has been written.

There are two main types of tests, both of which you should include in your code.

* Runtime (sanity) tests - these are light-weight tests performed while the code is running to ensure that everything is ok, e.g. arguments passed to a function make sense and are valid inputs.

* Correctness (unit) tests - these are heavier tests, typically run and written separately from the code, that test that the functions give the correct answers and behave in the expected way.

## Runtime tests

These are run in a function to ensure that the function is being called correctly with sensible (sane) arguments. For example, lets consider our [addArrays](addarrays.py) function from the last session.

    $ ipython
    $ from addarrays import *
    $ addArrays( [1,2,3], [4,5,6] )
    [5, 7, 9]

    $ addArrays( [1,2], [4,5,6] )
    [5, 7]

    $ addArrays( [1,2,3], [4,5] )
    ---------------------------------------------------------------------------
    IndexError                                Traceback (most recent call last)
    <ipython-input-4-de656a8188a3> in <module>()
    ----> 1 addarrays.addArrays( [1,2,3], [4,5] )
    
    /Users/chris/Work/Teaching/swcarpentry/exeter/2013-11-14-exeter/Python/addarrays.py in addArrays(a, b)
          7 
          8     for i in range(0,len(a)): 
    ----> 9         c.append( a[i] + b[i] )
         10 
         11     return c

    IndexError: list index out of range

addArrays expects both arrays to contain the same number of items. In the first case, the first array was smaller than the second, and this worked (surprisingly - but did it do what the user would expect? - should it have returned [5,7,6]?). In the second case, the function failed with a scary-looking error message.

To clean the function, we need to add a runtime test that checks that both arrays have the same length. If they don’t, then we need to report this back to the user using a sensible error message. We do this using an exception.

    $ def addArrays(a, b):
    $     “””Function to add together the two passed arrays, returning
    $        the result."""
    $
    $     if len(a) != len(b):
    $         raise ValueError("Both arrays must have the same length.")
    $
    $     c = []
    $
    $     for i in range(0,len(a)):
    $         c.append( a[i] + b[i] )
    $
    $     return c

Here, we raise a ValueError, which indicates that something is wrong with the Value of one of the arguments. A list of all Python exceptions is [here](http://docs.python.org/2/library/exceptions.html#exceptions.Exception). Also note that you can create your own exceptions as well, instructions [here](http://docs.python.org/2/tutorial/errors.html#user-defined-exceptions) (although this is beyond what we have time to cover today).

Now when we call the function incorrectly, we get a sensible error message…

    $ ipython
    $ from addarrays import *
    $ addArrays([1,2], [3,4,5])

    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    <ipython-input-2-fdd61ba0cb11> in <module>()
    ----> 1 addarrays.addArrays([1,2], [3,4,5])
    
    /Users/chris/Work/Teaching/swcarpentry/exeter/2013-11-14-exeter/Python/addarrays.py in addArrays(a, b)
          5 
          6     if len(a) != len(b):
    ----> 7         raise ValueError("Both arrays must have the same length.")
          8 
          9     c = []

    ValueError: Both arrays must have the same length.

The benefit of an exception, is that it provides a way for your function to test and report when something has gone wrong. If something has gone wrong, it can be reported back to the user with a sensible error message. Also, unlike just printing a message and exiting the program, exceptions provide a way to recover from errors. This is achieved using “try” blocks. For example;

    $ ipython
    $ from addarrays import *
    $
    $ a = [1,2]
    $ b = [3,4,5]
    $
    $ try:
    $     c = addArrays(a,b)
    $     print c
    $ except ValueError:
    $     print “Something went wrong calling addArrays”

    Something went wrong calling addArrays

A “try” block lets you try to run a piece of code. If an exception is raised, then the exception is caught in the “except” block. This can be used either to present an even cleaner error message, or to fix the problem, e.g.

    $ ipython
    $ from addarrays import *
    $
    $ a = [1,2]
    $ b = [3,4,5]
    $
    $ try:
    $     c = addArrays(a,b)
    $ except ValueError:
    $     while len(a) < len(b):
    $         a.append(0)
    $     while len(b) < len(a):
    $         b.append(0)
    $     c = addArrays(a,b)
    $
    $ print c

    [4, 6, 5]

So you can see that exceptions allow us to fix problems in the context of how the function is called. Note that it would not be appropriate to add this fix into addArrays itself, as addArrays cannot know itself whether or not the arrays contain numbers, or whether or not it would be appropriate to make the arrays equal by padding with zeroes. Only the code that calls addArrays knows the context of the call, and thus what an appropriate fix would be. Exceptions provide a way for addArrays to signal that a problem has occurred, and the “try” block provides the way for the caller to fix the problem.

## Correctness tests

The second set of tests are correctness (also called unit) tests. These are tests that are run on a function to test that it is giving the correct output. For example, we can test that addArrays is adding together numbers correctly using;

    $ ipython
    $ from addarrays import *
    $
    $ def test_addArrays():
    $     a = [1,2,3]
    $     b = [4,5,6]
    $     expect = [5,7,9]
    $     c = addArrays(a,b)
    $     if c == expect:
    $         print “OK”
    $     else:
    $         print “BROKEN”
    $
    $ test_addArrays()

    OK

Testing manually works but is time-consuming and error prone - we might forget to run a test. What we need is a way to collect together all of the tests and to automate them.

The first thing to do is to create a testing script for our module, which is typically called “test_MODULENAME.py”, so in our case, it would be “test_addarrays.py”. Into this file, we should add all of our tests, e.g.

    $ from addarrays import *
    $
    $ def test_add():
    $     a = [1,2,3]
    $     b = [4,5,6]
    $     expect = [5,7,9]
    $     c = addArrays(a,b)
    $     assert( expect == c )
 
The only change here is that we have used “assert”. This is a function that does nothing if the passed test is true, but that will raise an AssertationError exception if the test is false. We can run the test manually using ipython

    $ ipython
    $ from test_addarrays import *
    $ test_add()

This is still a bit manual. Fortunately, Python comes with “nosetests” which automates running test scripts like this. [nose](https://pypi.python.org/pypi/nose/) automatically finds, runs and reports on tests.
Type

    $ nosetests test_addarrays.py
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.004s
    
    OK

This automatically ran all functions that started with “test_”. You can check this by breaking the code, e.g.

    $ def addArrays(a, b):
    $     “””Function to add together the two passed arrays, returning
    $        the result."""
    $
    $     if len(a) != len(b):
    $         raise ValueError("Both arrays must have the same length.")
    $
    $     c = []
    $
    $     for i in range(0,len(a)):
    $         c.append( a[i] - b[i] )
    $
    $     return c

    $ nosetests test_addarrays.py
    F
    ======================================================================
    FAIL: test_addarrays.test_add
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/Library/Python/2.7/site-packages/nose-1.3.0-py2.7.egg/nose/case.py", line 197, in runTest
        self.test(*self.arg)
      File "/Users/chris/Work/Teaching/swcarpentry/exeter/2013-11-14-exeter/Python/test_addarrays.py", line 9, in test_add
        assert( expect == c )
    AssertionError

    ----------------------------------------------------------------------
    Ran 1 test in 0.005s

    FAILED (failures=1)

## Exercise 4a

Expand test_addarrays.py with more tests, e.g. a function to test that addArrays correctly adds together arrays of negative numbers, a function to test that addArrays correctly adds arrays of strings, a function to test that addArrays correctly adds together empty arrays. Try to think of all of the things that could break the code. Also add a function that tests that addArrays correctly reports when the arrays are the wrong size, e.g.

    $ def test_wrongsize():
    $     a = [1,2,3]
    $     b = [4,5]
    $     try:
    $         addArrays(a,b)
    $         assert(False)
    $     except ValueError:
    $         assert(True)

Run your tests with “nosetests”. 

If you get stuck, an example test script is [here](python_testing/test_addarrays1.py)

## When 1 + 1 = 2.0000001

Computers don't do floating point arithmetic too well.

    $ ipython
    $ expected = 0
    $ actual = 0.1 + 0.1 + 0.1 - 0.3
    $ assert(expected == actual)

    ---------------------------------------------------------------------------
    AssertionError                            Traceback (most recent call last)
    <ipython-input-3-18a1029b2615> in <module>()
    ----> 1 assert(expected == actual)

    AssertionError: 

    $ print actual

    5.55111512313e-17

Compare to within a threshold, or delta e.g. expected == actual  if expected - actual < 0.0000000000000001.

Thresholds are application-specific. 

    $ from nose.tools import assert_almost_equal
    $ assert_almost_equal(expected, actual, 0)
    
    $ assert_almost_equal(expected, actual, 10)
    
    $ assert_almost_equal(expected, actual, 15)
    
    $ assert_almost_equal(expected, actual, 16)

    ---------------------------------------------------------------------------
    AssertionError                            Traceback (most recent call last)
    <ipython-input-9-df3b297d7739> in <module>()
    ----> 1 assert_almost_equal(expected, actual, 16)

    /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/unittest/case.pyc in assertAlmostEqual(self, first, second, places, msg, delta)
        561                                                           places)
        562         msg = self._formatMessage(msg, standardMsg)
    --> 563         raise self.failureException(msg)
        564 
        565     def assertNotAlmostEqual(self, first, second, places=None, msg=None, delta=None):
    
    AssertionError: 0 != 5.551115123125783e-17 within 16 places

## Exercise 4b

Add in tests for floating point addition, using assert_almost_equal. Note that you will need to test each element of the array, one by one.

If you get stuck, an example test script is [here](python_testing/test_addarrays2.py).

## When should we test?

* Always!
* Early, and not wait till after we've used it to generate data for our important paper, or given it to someone else to use.
* Often, so that we know that any changes we've made to our code, or to things that our code needs (e.g. libraries, configuration files etc.) haven't introduced any bugs.
* Before writing the code. The best order to write a function is to write the function documentation, then a function signature, then the tests for a function, and then the function itself. Documentation first, as then you know what the function should do. Then the signature, so you know what it is called and what it takes as input. Then tests, as you then specify what should be returned, and then finally the code itself to actually do all of the work and pass all of your tests. While this may sound long-winded, writing tested, documented code now that works now and can be tested to work for all time is better than writing untested, undocumented code that you will spend the next few years debugging.. and that you suddenly realise is giving the wrong results just before you submit your thesis or Nature paper..!

How much is enough? 

What we know about software development - we can't test everything. 

No excuse for testing nothing! Learn by experience, like writing a paper.

Review tests, like code, to avoid

* Pass when they should fail, false positives.
* Fail when they should pass, false negatives.
* Don't test anything. 

Example.

    def test_critical_correctness():
        # TODO - will complete this tomorrow!
        pass

## Summary

Testing

* Saves time.
* Gives confidence that code does what we want and expect it to.
* Promotes trust that code, and so research, is correct.
* Mirrors your documentation. Documentation provides the promise of what the code will do. Tests provide the proof.

## Links

* [Software Carpentry](http://software-carpentry.org/)'s online [testing](http://software-carpentry.org/4_0/test/index.html) lectures.
* A discussion on [is it worthwhile to write unit tests for scientific research codes?](http://scicomp.stackexchange.com/questions/206/is-it-worthwhile-to-write-unit-tests-for-scientific-research-codes)
* G. Wilson, D. A. Aruliah, C. T. Brown, N. P. Chue Hong, M. Davis, R. T. Guy, S. H. D. Haddock, K. Huff, I. M. Mitchell, M. Plumbley, B. Waugh, E. P. White, P. Wilson (2012) "[Best Practices for Scientific Computing](http://arxiv.org/abs/1210.0530)", arXiv:1210.0530 [cs.MS].
