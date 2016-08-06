#!/usr/bin/env python

from __future__ import print_function, division

from peModules.factorization import proper_divisors
from peModules.primality import is_prime

def sum_proper_divisors(n):
    list_proper_divisors = proper_divisors(n)
    sum_to_return = 0
    for proper_divisor in list_proper_divisors:
        sum_to_return += proper_divisor
    return sum_to_return

def amicable_pair(n):
    if (is_prime(n)):
        return 0
    elif (sum_proper_divisors(sum_proper_divisors(n)) == n):
        if (sum_proper_divisors(n) == n):
            return 0
        else:
            return sum_proper_divisors(n)
    else:
        return 0
    
if __name__ == "__main__":
    test_number = 2
    list_so_far=[]
    while (test_number < 10000):
        if (test_number in list_so_far):
            test_number += 1
            continue
        else:
            amicable = amicable_pair(test_number)
            if (amicable>0):
                print ("Amicable pair: (%i,%i)"%(test_number,amicable))
                list_so_far.extend([test_number,amicable])
            test_number += 1
    print ("List of amicable numbers below 10000 is %s and their sum is %d"%(list_so_far,sum(list_so_far)))
