#!/usr/bin/env python

from __future__ import print_function, division

from utilities import get_list_of_digits
from rationalNumber import rationalNumber

def isTrivialSelfCancelling(numerator, denominator):
    if (numerator%11 == 0 and denominator%11 == 0):
        return True
    if (numerator%10 == 0 and denominator%10 == 0):
        return True
    if (numerator == denominator):
        return True
    return False

def isNontrivialSelfCancelling(numerator, denominator):
    if (isTrivialSelfCancelling(numerator, denominator)):
        return False

    numerator_list_of_digits = get_list_of_digits(numerator)
    denominator_list_of_digits = get_list_of_digits(denominator)

    original_fraction = rationalNumber(numerator, denominator, True)

    combination1 = rationalNumber(1, 1, False)
    combination2 = rationalNumber(1, 1, False)
    combination3 = rationalNumber(1, 1, False)
    combination4 = rationalNumber(1, 1, False)

    if (numerator_list_of_digits[1]==denominator_list_of_digits[1]):
        combination1 = rationalNumber(numerator_list_of_digits[0], denominator_list_of_digits[0], True)
    if (numerator_list_of_digits[0]==denominator_list_of_digits[1]):
        combination2 = rationalNumber(numerator_list_of_digits[1], denominator_list_of_digits[0], True)
    if (denominator_list_of_digits[1] > 0):
        if (numerator_list_of_digits[1]==denominator_list_of_digits[0]):
            combination3 = rationalNumber(numerator_list_of_digits[0], denominator_list_of_digits[1], True)
        if (numerator_list_of_digits[0]==denominator_list_of_digits[0]):
            combination4 = rationalNumber(numerator_list_of_digits[1], denominator_list_of_digits[1], True)

    if (original_fraction == combination1 or original_fraction == combination2 or original_fraction == combination3 or original_fraction == combination4):
        return True
    return False

if __name__ == "__main__":
    required_product = rationalNumber(1,1,True)
    for denominator in range(11, 99):
        for numerator in range(11, 1+denominator):
            if (isNontrivialSelfCancelling(numerator, denominator)):
                selfCancellingFraction = rationalNumber(numerator,denominator,True)
                print ("The following nontrivial fraction is self cancelling:")
                print (selfCancellingFraction)
                required_product *= selfCancellingFraction
    print ("Required product:")
    print (required_product)
