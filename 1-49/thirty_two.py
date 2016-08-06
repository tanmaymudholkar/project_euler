#!/usr/bin/env python

from __future__ import print_function, division

from peModules.factorization import get_all_factors
from peModules.miscellaneous import get_list_of_digits

def is_pandigital_product(candidate):
    candidate_list_of_digits = get_list_of_digits(candidate)
    
    if (len(candidate_list_of_digits) != len(set(candidate_list_of_digits)) or 0 in candidate_list_of_digits):
        return False

    candidate_list_of_factors = get_all_factors(candidate)
    for factor in candidate_list_of_factors:
        if (factor <= candidate//2):
            complete_list_of_digits = candidate_list_of_digits + get_list_of_digits(factor) + get_list_of_digits(candidate//factor)
            if (len(set(complete_list_of_digits)) == 9 and 0 not in complete_list_of_digits):
                print ("%d satisfies the condition: %d = %d * %d"%(candidate, candidate, factor, candidate//factor))
                return True
    return False

if __name__ == "__main__":
    sum_pandigitals_1_through_9 = 0
    for candidate in range(1000,9999):
        if is_pandigital_product(candidate):
            sum_pandigitals_1_through_9 += candidate
    print ("Sum of all integers of required type: %d"%(sum_pandigitals_1_through_9))
