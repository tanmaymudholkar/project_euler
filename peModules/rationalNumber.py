from __future__ import print_function, division

from factorization import get_prime_factors
from miscellaneous import get_gcd

class rationalNumber:
    def __init__(self, original_numerator=0, original_denominator=1, isPositiveOrZero=True):
        if (original_numerator < 0 or not(isinstance(original_numerator, int) or isinstance(original_numerator,long))):
            raise TypeError('Only zero or positive integers allowed for numerator!')
        if (original_denominator < 1 or not(isinstance(original_denominator, int) or isinstance(original_denominator,long))):
            raise TypeError('Only positive integers allowed for denominator!')
        if (not(isinstance(isPositiveOrZero,bool))):
            raise TypeError('Only True = positive or 0, or False=negative, allowed for sign')
        self.original_numerator = original_numerator
        self.original_denominator = original_denominator
        self.isPositiveOrZero = isPositiveOrZero
        gcd = get_gcd(original_numerator, original_denominator)
        if (gcd > 0):
            self.numerator = original_numerator // gcd
            self.denominator = original_denominator // gcd
        else:
            self.numerator = 0
            self.denominator = 1

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if (self.numerator == other.numerator and self.denominator == other.denominator and self.isPositiveOrZero == other.isPositiveOrZero):
                return True
            if (self.numerator == 0 and other.numerator == 0):
                return True
        else:
            return False

    def __ne__(self, other):
        return (not(self.__eq__(other)))

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            if (self.isPositiveOrZero and not(other.isPositiveOrZero)):
                return True
            elif (other.isPositiveOrZero and not(self.isPositiveOrZero)):
                return False
            elif (self.isPositiveOrZero):
                return (self.numerator*other.denominator > self.denominator*other.numerator)
            else:
                return (self.numerator*other.denominator < self.denominator*other.numerator)
        else:
            raise TypeError("Two objects belong to different classes and cannot be compared")

    def __lt__(self, other):
        return (not(self.__gt__(other)) and self.__ne__(other))

    def __ge__(self, other):
        return (not(self.__lt__(other)))

    def __le__(self, other):
        return (not(self.__gt__(other)))

    def __add__(self, other):
        if isinstance(other, self.__class__):
            result_denominator = self.denominator*other.denominator
            result_isPositiveOrZero = True
            result_numerator = 0
            if ((self.isPositiveOrZero and other.isPositiveOrZero) or (not(self.isPositiveOrZero) and not(other.isPositiveOrZero))):
                result_isPositiveOrZero = self.isPositiveOrZero
                result_numerator = self.numerator*other.denominator + self.denominator*other.numerator
            else:
                result_numerator = self.numerator*other.denominator - self.denominator*other.numerator
                if (other.isPositiveOrZero):
                    result_numerator = -result_numerator
                if (result_numerator < 0):
                    result_numerator = -result_numerator
                    result_isPositiveOrZero = False
            return rationalNumber(result_numerator, result_denominator, result_isPositiveOrZero)
        else:
            raise TypeError("Two objects belong to different classes and cannot be added or subtracted")

    def __sub__(self, other):
        other_with_inverted_sign = rationalNumber(other.numerator, other.denominator, not(other.isPositiveOrZero))
        return self.__add__(other_with_inverted_sign)

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return rationalNumber(self.numerator*other.numerator, self.denominator*other.denominator, (self.isPositiveOrZero and other.isPositiveOrZero) or (not(self.isPositiveOrZero) and not(other.isPositiveOrZero)))
        else:
            raise TypeError("Two objects belong to different classes and cannot be multiplied")

    def __div__(self, other):
        if isinstance(other, self.__class__):
            return rationalNumber(self.numerator*other.denominator, self.denominator*other.numerator, (self.isPositiveOrZero and other.isPositiveOrZero) or (not(self.isPositiveOrZero) and not(other.isPositiveOrZero)))
        else:
            raise TypeError("Two objects belong to different classes and one cannot divide the other")

    def __abs__(self):
        return rationalNumber(self.numerator, self.denominator, True)

    def __repr__(self):
        if (self.isPositiveOrZero):
            sign=''
        else:
            sign='-'
        return "Member of class rationalNumber. Originally: %s %d/%d, reduced: %s %d/%d"%(sign, self.original_numerator, self.original_denominator, sign, self.numerator, self.denominator)
