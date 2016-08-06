#!/usr/bin/env python

from __future__ import division
from __future__ import print_function

import math

if __name__=="__main__":
    digits_to_sum=math.factorial(100)
    sum_of_digits=0
    while digits_to_sum>0:
        sum_of_digits += digits_to_sum%10
        digits_to_sum //= 10
    print ("Sum is %i"%(sum_of_digits))
