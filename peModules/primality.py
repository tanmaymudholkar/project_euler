from __future__ import print_function, division

import math

def is_prime(number_to_check):
    if (not(isinstance(number_to_check, int))):
        raise TypeError('Primality only defined for integers!')
    if (number_to_check < 1):
        raise ValueError('Integer needs to be greater than or equal to 1!')
    if (number_to_check==1):
        return False
    if (number_to_check==2):
        return True
    elif (number_to_check==3):
        return True
    elif (number_to_check%2 == 0):
        return False
    elif (number_to_check%3 == 0):
        return False
    else:
        putative_factor = 5
        to_increment_by = 2
        limit_up_to_which_to_check = int(math.floor(math.sqrt(number_to_check)))
        while(putative_factor <= limit_up_to_which_to_check):
            if (number_to_check%putative_factor == 0):
                return False
            else:
                putative_factor += to_increment_by
                to_increment_by = 6-to_increment_by

        return True
