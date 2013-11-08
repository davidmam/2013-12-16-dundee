
def addArrays(a, b):
    """Function to add together the two passed arrays, returning
       the result."""

    c = []

    for i in range(0,len(a)):
        c.append( a[i] + b[i] )

    return c
