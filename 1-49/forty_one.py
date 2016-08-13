#!/usr/bin/env python

from __future__ import print_function, division

from peModules.primality import is_prime

def pandigitalStrGenerator(listRemainingDigits):
    if len(listRemainingDigits) == 0:
        yield ""
    else:
        for digitIndex in range(len(listRemainingDigits)):
            digitChosen = listRemainingDigits[digitIndex]
            listNewRemainingDigits = listRemainingDigits[:digitIndex]+listRemainingDigits[1+digitIndex:]
            for remainingStr in pandigitalStrGenerator(listNewRemainingDigits):
                yield str(digitChosen)+remainingStr

if __name__ == "__main__":
    pandigitalPrimePossibilitiesForNumberOfDigits = list(reversed([4,7]))
    for possibilityForNumberOfDigits in pandigitalPrimePossibilitiesForNumberOfDigits:
        largestPandigitalFound = False
        for pandigitalStr in pandigitalStrGenerator(list(reversed(range(1,1+possibilityForNumberOfDigits)))):
            pandigital = int(pandigitalStr)
            print ("Checking %d:"%(pandigital))
            if (is_prime(pandigital)):
                print ("Largest pandigital prime is %d"%(pandigital))
                largestPandigitalFound = True
                break
        if (largestPandigitalFound):
            break
