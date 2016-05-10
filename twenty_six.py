#!/usr/bin/env python

from __future__ import print_function, division

from factorization import get_prime_factorization
from utilities import get_number_of_digits
from math import floor

def reciprocal_is_recurring(n):
    list_of_prime_factors = get_prime_factorization(n).primefactors
    if (list_of_prime_factors == [2] or list_of_prime_factors == [5] or list_of_prime_factors == [2,5]):
        return False
    else:
        return True

# def get_ith_digit_in_decimal_expansion_of_reciprocal_of_n(n, i, carried_remainder):
#     carried_remainder *= 10
#     return [carried_remainder // n, ]

def get_digit_and_remainder(numerator_digit, remainder_from_previous_digit, denominator):
    return [(remainder_from_previous_digit * 10 + numerator_digit) // denominator, (remainder_from_previous_digit * 10 + numerator_digit) % denominator]
        
def get_maximal_list_of_repeating_digits(n):
    if (reciprocal_is_recurring(n)):
        maximum_size_of_pattern = n-1
        no_of_digits = get_number_of_digits(n)
        number_of_places_after_decimal_point_at_which_to_start = 2*no_of_digits
        # list_of_digits = []
        # for index in range(number_of_places_after_decimal_point_at_which_to_start, number_of_places_after_decimal_point_at_which_to_start + maximum_size_of_pattern + 1):
        #     list_of_digits.append(get_ith_digit_in_decimal_expansion_of_n(1/n, index))
        list_of_digits = []
        numerator_digit = 1
        remainder_from_previous_digit = 0
        denominator = n
        digit_and_remainder = get_digit_and_remainder(numerator_digit, remainder_from_previous_digit, denominator)
        numerator_digit = digit_and_remainder[0]
        remainder_from_previous_digit = digit_and_remainder[1]
        for disregard_counter in range(0, number_of_places_after_decimal_point_at_which_to_start):
            digit_and_remainder = get_digit_and_remainder(0, remainder_from_previous_digit, denominator)
            numerator_digit = digit_and_remainder[0]
            remainder_from_previous_digit = digit_and_remainder[1]
            
        for digit_counter in range(0,2*maximum_size_of_pattern):
            digit_and_remainder = get_digit_and_remainder(0, remainder_from_previous_digit, denominator)
            numerator_digit = digit_and_remainder[0]
            list_of_digits.append(numerator_digit)
            remainder_from_previous_digit = digit_and_remainder[1]
        return list_of_digits
    else:
        return [0]

def get_recurring_cycle(n):
    if (reciprocal_is_recurring(n)):    
        maximal_list_of_repeating_digits = get_maximal_list_of_repeating_digits(n)
        maximum_size_of_pattern = len(maximal_list_of_repeating_digits) // 2
        number_of_elements_in_putative_recurrence = 1
        while (number_of_elements_in_putative_recurrence <= maximum_size_of_pattern):
            putative_recurrence = [maximal_list_of_repeating_digits[index] for index in range(0,number_of_elements_in_putative_recurrence)]
            recurs = True
            index = number_of_elements_in_putative_recurrence
            while(index + number_of_elements_in_putative_recurrence < maximum_size_of_pattern*2):
                list_to_check_against = [maximal_list_of_repeating_digits[checking_index] for checking_index in range(index, index + number_of_elements_in_putative_recurrence)]
                if (putative_recurrence == list_to_check_against):
                    index += number_of_elements_in_putative_recurrence
                    continue
                else:
                    recurs = False
                    break
            if (recurs):
                recurrence = putative_recurrence
                break
            else:
                number_of_elements_in_putative_recurrence += 1
                continue
        return recurrence
    else:
        return [0]

def get_length_of_recurring_cycle(n):
    return len(get_recurring_cycle(n))

if __name__ == "__main__":
    for n in range(2,1000):
        print ("For n = %i, recurring cycle is %s and its length is %i"%(n, get_recurring_cycle(n),get_length_of_recurring_cycle(n)))
