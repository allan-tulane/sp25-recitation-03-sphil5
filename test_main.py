from main import *



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert quadratic_multiply(BinaryNumber(7), BinaryNumber(7)) == 7*7
    assert quadratic_multiply(BinaryNumber(5), BinaryNumber(8)) == 5*8
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(7)) == 2*7
