
from addarrays import *

def test_add():
    a = [1,2,3]
    b = [4,5,6]
    expect = [5,7,9]
    c = addArrays(a,b)
    assert( expect == c )

