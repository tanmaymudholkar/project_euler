#!/usr/bin/env python

from __future__ import division, print_function
from sys import exit
from math import ceil

def getDenominatorExponentOfTen(naturalNumber):
    m = naturalNumber
    n = len(str(naturalNumber)) - 1
    powerNumerator = 9*m*(1+n) - 10**(n+1) + 9*n + 10
    return (powerNumerator//9)

def getContributingExponent(decimalPosition):
    numberOfDigits = 0
    while True:
        denominatorExponentOfTen = getDenominatorExponentOfTen(10**numberOfDigits)
        if denominatorExponentOfTen == decimalPosition:
            return 10**numberOfDigits
        if denominatorExponentOfTen > decimalPosition:
            break
        numberOfDigits += 1
    contributingExponentNumerator = 9*decimalPosition + 10**(numberOfDigits) - 9*numberOfDigits - 1
    contributingExponentDenominator = 9*numberOfDigits
    if contributingExponentNumerator%contributingExponentDenominator == 0:
        return contributingExponentNumerator//contributingExponentDenominator
    contributingExponent = int(ceil(contributingExponentNumerator/contributingExponentDenominator))
    return contributingExponent

def getDigit(decimalPosition):
    contributingExponent = getContributingExponent(decimalPosition)
    newContributingExponent = contributingExponent
    shiftIndex = 0
    while newContributingExponent==contributingExponent:
        shiftIndex += 1
        newContributingExponent = getContributingExponent(decimalPosition + shiftIndex)
    return int(str(contributingExponent)[-shiftIndex])

if __name__ == "__main__":
    requiredProduct = 1
    for powerOfTen in range(0,7):
        decimalPosition = 10**powerOfTen
        digit = getDigit(decimalPosition)
        requiredProduct *= digit
    print ("Required product is %d"%(requiredProduct))
