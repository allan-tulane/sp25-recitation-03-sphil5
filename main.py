"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
    # this just converts the result from a BinaryNumber to a regular int
    return _quadratic_multiply(x,y).decimal_val

def _quadratic_multiply(x, y):
    ### TODO
    ## obtains the yvec and xvec binary vectors of x and y 
    x = x.binary2int(x.binary_vec)
    y = y.binary2int(y.binary_vec)

    result = BinaryNumber(0)

    ## loop through the bits of x 
    for i in range(len(x.binary_vec) - 1, -1, -1):
        ## if the bit is 1, we are going to shift y by i
        if x.binary_vec[i] == 1:
            ## result = result + y
            ## y = y + y
            yshift = bit_shift(y, len(x.binary_vec) - 1 - i)
            ## add the shifted y to the result 
            result = result + yshift 
            
    return result
    ###


    
    
def test_quadratic_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    
    return (time.time() - start)*1000


    
    

