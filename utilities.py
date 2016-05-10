from __future__ import print_function, division

def get_number_of_digits(n):
    number_of_digits_so_far = 0
    while (n != 0):
        n //= 10
        number_of_digits_so_far += 1
    return number_of_digits_so_far

def get_list_of_digits(n):
    list_of_digits = []
    while (n != 0):
        list_of_digits.append(n % 10)
        n //= 10
    list_of_digits.reverse()
    return list_of_digits

def get_sum_of_nth_powers(list_of_digits, n):
    sum_of_nth_powers = 0
    for digit in list_of_digits:
        sum_of_nth_powers += digit**n
    return sum_of_nth_powers
