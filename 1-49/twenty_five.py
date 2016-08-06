#!/usr/bin/env python

from __future__ import print_function, division

from peModules.fibonacci import fib

def number_of_digits(n):
    number_of_digits_so_far = 0
    while (n != 0):
        n //= 10
        number_of_digits_so_far += 1
    return number_of_digits_so_far
    
if __name__ == "__main__":
    digits = 1
    index = 1
    while(digits < 1000):
        digits = number_of_digits(fib(index))
        index += 1
    print ("required index = %i"%(index-1))
