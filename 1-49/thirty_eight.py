#!/usr/bin/env python

from __future__ import print_function, division
from sys import exit

targetList = range(1,10)
targetSet = set(targetList)

def isPandigital(candidateList):
    if (set(candidateList) == targetSet):
        return True
    return False

def getListOfDigitsInConcatenatedProduct(seed):
    seedList = list(str(seed))
    if (len(seedList) < 4):
        exit("Outside intended range")
    seedTimesTwo = seed*2
    seedTimesTwoList = list(str(seedTimesTwo))
    resultList = [int(digitStr) for digitStr in (seedList+seedTimesTwoList)]
    return resultList

if __name__ == "__main__":
    greatestCandidate = 0
    maximalListOfDigits = []
    for candidate in range(9182,9877):
        listOfDigitsInConcatenatedProduct = getListOfDigitsInConcatenatedProduct(candidate)
        if (isPandigital(listOfDigitsInConcatenatedProduct)):
            greatestCandidate = candidate
            maximalListOfDigits = listOfDigitsInConcatenatedProduct
    print ("Greatest candidate is %d"%(greatestCandidate))
