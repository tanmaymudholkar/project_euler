#!/usr/bin/env python

from __future__ import division, print_function

import math

def permutation(permutation_number, list_of_remaining_digits, number_of_remaining_digits):
    if (number_of_remaining_digits == 1):
        if (len(list_of_remaining_digits) == 1):
            return list_of_remaining_digits
        else:
            return "More than one element remaining?"
    else:
        broad_position = (permutation_number - 1) // math.factorial(number_of_remaining_digits - 1)
        permutation_to_return = [list_of_remaining_digits[broad_position]] # Before extending
        del list_of_remaining_digits[broad_position]
        narrow_position = permutation_number % math.factorial(number_of_remaining_digits - 1)
        if (narrow_position == 0):
            narrow_position = math.factorial(number_of_remaining_digits - 1)
        permutation_to_return.extend(permutation(narrow_position, list_of_remaining_digits, number_of_remaining_digits - 1))
        return permutation_to_return

if __name__ == "__main__":
    list_of_remaining_digits = range(0,10)
    number_of_remaining_digits = len(list_of_remaining_digits)
    permutation_number = 1000000
    required_permutation = permutation(permutation_number, list_of_remaining_digits, number_of_remaining_digits)
    print ("Permutation number %d: %s"%(permutation_number, required_permutation))
