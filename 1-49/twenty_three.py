#!/usr/bin/env python

from __future__ import print_function, division

from peModules.factorization import proper_divisors

def perfectness(n):
    list_of_proper_divisors = proper_divisors(n)
    sum_of_proper_divisors = sum(list_of_proper_divisors)
    if (sum_of_proper_divisors == n):
        return 0
    elif (sum_of_proper_divisors < n):
        return -1
    else:
        return 1

def populate_abundance_list():
    global list_of_abundant_numbers
    list_of_abundant_numbers = []
    for i in range(2, 28124):
        if (perfectness(i) == 1):
            list_of_abundant_numbers.append(i)

# def generate_abundant_pairs():
#     for index_1 in range(0, len(list_of_abundant_numbers)):
#         for index_2 in range(index_1, len(list_of_abundant_numbers)):
#             yield [list_of_abundant_numbers[index_1], list_of_abundant_numbers[index_2]]

def can_be_expressed_as_sum_of_two_abundant_numbers(n):
    can_be_expressed = False
    abundance_list_counter = 0
    current_abundant_element = list_of_abundant_numbers[abundance_list_counter]
    while(current_abundant_element <= n//2):
        potential_mate = n - current_abundant_element
        if (potential_mate in list_of_abundant_numbers):
            can_be_expressed = True
            break
        else:
            abundance_list_counter += 1
            if (abundance_list_counter >= len(list_of_abundant_numbers)):
                break
            else:
                current_abundant_element = list_of_abundant_numbers[abundance_list_counter]
    return can_be_expressed

def calculate_required_sum():
    required_sum = 0
    for candidate in range(1, 28124):
        if (not(can_be_expressed_as_sum_of_two_abundant_numbers(candidate))):
            print ("%d cannot be expressed as a sum of two abundant numbers"%(candidate))
            required_sum += candidate
    return required_sum

if __name__ == "__main__":
    populate_abundance_list()
    # print ("List of abundant numbers is %s"%(list_of_abundant_numbers))
    # set_of_numbers_that_cannot_be_expressed_as_sum_of_abundant_pair = set(range(0,28124))
    # abundant_pair_generator = generate_abundant_pairs()
    # for abundant_pair in abundant_pair_generator:
    #     abundant_pair_sum_set = set([abundant_pair[0] + abundant_pair[1]])
    #     set_of_numbers_that_cannot_be_expressed_as_sum_of_abundant_pair = set_of_numbers_that_cannot_be_expressed_as_sum_of_abundant_pair - abundant_pair_sum_set
    # list_of_numbers_that_cannot_be_expressed_as_sum_of_abundant_pair = list(set_of_numbers_that_cannot_be_expressed_as_sum_of_abundant_pair)
    # print ("List of numbers that cannot be expressed as sum of an abundant pair is %s"%(list_of_numbers_that_cannot_be_expressed_as_sum_of_abundant_pair))
    required_sum = calculate_required_sum()
    print ("Required sum is %i"%(required_sum))
