#!/usr/bin/python3
# Author - Tolulope Fakunle
"""print the numbers from 1 to 100 seperated by space.
    For multples of three, print Fizz.
    For multiples of five, print Buzz.
    For multiples of fie and three, print FizzBuzz.
     """
def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="" )
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), ends="")
       
