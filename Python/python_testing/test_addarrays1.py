
from addarrays import *

def test_add():
    a = [1,2,3]
    b = [4,5,6]
    expect = [5,7,9]
    c = addArrays(a,b)
    assert( expect == c )

def test_addneg():
    a = [-1, -2, -3]
    b = [-4, -5, -6]
    expect = [-5, -7, -9]
    c = addArrays(a,b)
    assert( expect == c )

def test_addstrings():
    a = ["Hello ", "ice-", "tea"]
    b = ["World", "cream", "bag"]
    expect = [ "Hello World", "ice-cream", "teabag" ]
    c = addArrays(a,b)
    assert( expect == c )

def test_addempty():
    a = []
    b = []
    expect = []
    c = addArrays(a, b)
    assert( expect == c )

def test_wrongsize():
    a = [1,2,3]
    b = [4,5]
    try:
        addArrays(a,b)
        assert(False)
    except ValueError:
        assert(True)

