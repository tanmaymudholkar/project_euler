#!/usr/bin/env python

from __future__ import division, print_function

from primality import is_prime

def quadratic_form(a,b,n):
    return (n**2 + a*n + b)

def get_number_of_consecutive_primes(a,b):
    n = 0
    while (is_prime(quadratic_form(a,b,n))):
        n += 1
    return n

if __name__ == "__main__":
    maximum_number_of_primes = 0
    product_at_maximum = 1
    for a in range(-999,1000):
        for b in range(-999,1000):
            number_of_consecutive_primes = get_number_of_consecutive_primes(a,b)
            if (number_of_consecutive_primes > maximum_number_of_primes):
                maximum_number_of_primes = number_of_consecutive_primes
                product_at_maximum = a*b
    print ("Product at maximum number of consecutive primes is %i"%(product_at_maximum))
