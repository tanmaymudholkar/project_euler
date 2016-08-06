#!/usr/bin/env python

from __future__ import print_function, division
from peModules.miscellaneous import get_list_of_digits, get_sum_of_nth_powers

# Only up to 6 digits possible because we seek a number with m digits where:
# 10**m*a_m + 10**(m-1)*a_(m-1) + ... + a_0 = a_m**5 + a_(m-1)**5 + ... + (a_0)**5
# max rhs >= min lhs => (m+1)*9**5 >= 10**m
# The other condition, max lhs >= min rhs, does not give anything nontrivial.
# Above was not very well thought out.

def generate_required_list():
    for number in range(10, 1000000):
        list_of_digits = get_list_of_digits(number)
        sum_of_fifth_powers = get_sum_of_nth_powers(list_of_digits, 5)
        if (sum_of_fifth_powers == number):
            yield number
        else:
            continue

if __name__ == "__main__":
    required_list = generate_required_list()
    required_sum = 0
    for possibility in required_list:
        print ("One possibility is %i"%(possibility))
        required_sum += possibility
    print ("Required sum is %i"%(required_sum))
