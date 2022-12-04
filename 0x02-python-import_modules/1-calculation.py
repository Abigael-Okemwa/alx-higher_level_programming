#!/usr/bin/python

if __name__ = "__main__":
    """Print the sum, difference, multiplication and quotient of 10 and 5."""
    from calculator_1 import add, subtraction, multiplication, divide
    a = 10
    b = 5
    
    print("{} + {}".format(a, b, add(a, b)))
    print("{} - {}".format(a, b, subtract(a, b)))
    print("{} * {}".format(a, b, multiplication(a, b)))
    print("{} / {}".format(a, b, divide(a, b,)))
