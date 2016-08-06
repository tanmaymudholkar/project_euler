#!/usr/bin/env python

from __future__ import print_function, division

from peModules.miscellaneous import isPalindrome, palindromicNumberGenerator

if __name__ == "__main__":
    maxNDigits = 6
    requiredSum = 0
    for palindromicNumber in palindromicNumberGenerator(maxNDigits):
        listCandidateBin = list("{0:b}".format(palindromicNumber))
        if isPalindrome(listCandidateBin):
            print ("%d is palindromic in the fashion stated"%(palindromicNumber))
            requiredSum += palindromicNumber

    print ("Required sum is %d"%(requiredSum))
