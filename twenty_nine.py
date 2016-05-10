#!/usr/bin/env python

from __future__ import print_function, division

# Wrong approach:

# from primality import is_prime
# from factorization import get_prime_factorization
# # from math import ceil

# def generate_distinct_combinations(amin, amax, bmin, bmax):
#     for a in range(amin, 1 + amax):
#         if (is_prime(a)):
#             for b in range(bmin, 1 + bmax):
#                 yield a**b
#         else:
#             prime_factorization_of_a = get_prime_factorization(a)
#             prime_factors_of_a = prime_factorization_of_a.primefactors
#             if (len(prime_factors_of_a) == 1):
#                 exponents_of_a = prime_factorization_of_a.exponents
#                 power_of_earlier_prime = exponents_of_a[0]
#                 new_range_min = 1 + (bmax // power_of_earlier_prime)
#                 for b in range(new_range_min, 1 + bmax):
#                     yield a**b
#             else:
#                 for b in range(bmin, 1 + bmax):
#                     yield a**b

# def get_required_number(amin, amax, bmin, bmax):
#     distinct_combinations = list(generate_distinct_combinations(amin, amax, bmin, bmax))
#     print ("Distinct combinations are %s"%(distinct_combinations))
#     return len(distinct_combinations)

# New, quick-and-stupid approach:

def get_required_number(amin, amax, bmin, bmax):
    required_list = []
    for a in range(amin, 1 + amax):
        for b in range(bmin, 1 + bmax):
            required_list.append(a**b)
    required_list.sort()
    required_unique_list = [required_list[0]]
    for i in range (1, len(required_list)):
        if (required_list[i] == required_unique_list[-1]):
            continue
        else:
            required_unique_list.append(required_list[i])
    # print ("Unique list is %s"%(required_unique_list))
    return len(required_unique_list)

if __name__ == "__main__":
    required_number = get_required_number(2, 100, 2, 100)
    print ("Required number is %i"%(required_number))
