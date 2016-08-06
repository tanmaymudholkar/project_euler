#!/usr/bin/env python

from __future__ import division, print_function
import math
from peModules.miscellaneous import get_list_of_digits

# populate dictionary
digitFactorials = {digit:math.factorial(digit) for digit in range(0,10)}

def sumDigitFactorials(candidate):
    list_of_digits = get_list_of_digits(candidate)
    sumDigitFactorials = 0
    for digit in list_of_digits:
        sumDigitFactorials += digitFactorials[digit]
    return sumDigitFactorials
        
if __name__=="__main__":
    requiredSum = 0
    for candidate in range(11,1000000):
        if (candidate%10000 == 0):
            print ("Approximately %d percent complete"%(candidate//10000))
        if (sumDigitFactorials(candidate) == candidate):
            print ("%d is curious"%(candidate))
            requiredSum += candidate
    print ("Required sum is %d"%(requiredSum))
