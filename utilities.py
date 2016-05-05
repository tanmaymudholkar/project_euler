from __future__ import print_function, division

def number_of_digits(n):
    number_of_digits_so_far = 0
    while (n != 0):
        n //= 10
        number_of_digits_so_far += 1
    return number_of_digits_so_far
