#!/usr/bin/env python

from __future__ import print_function, division

from peModules.permutations_and_combinations import listCyclicPermutationGenerator
from peModules.primality import is_prime
from peModules.miscellaneous import get_list_of_digits, getNumberFromListOfDigits

if __name__ == "__main__":
    calculate_upto = 1000000
    listOfCyclicPrimes = []
    for candidate in range(1, min(calculate_upto,10)):
        if (is_prime(candidate)):
            listOfCyclicPrimes.append(candidate)
    if (calculate_upto >= 11):
        for candidate in range(10,1+calculate_upto):
            if candidate not in listOfCyclicPrimes:
                allCyclicPrime = True
                candidateCyclicNumbers = []
                for cyclicPermutation in listCyclicPermutationGenerator(get_list_of_digits(candidate)):
                    cyclicNumber = getNumberFromListOfDigits(cyclicPermutation)
                    candidateCyclicNumbers.append(cyclicNumber)
                    if (not(is_prime(cyclicNumber))):
                        allCyclicPrime = False
                        break
                if (allCyclicPrime):
                    for cyclicNumber in candidateCyclicNumbers:
                        if (cyclicNumber not in listOfCyclicPrimes):
                            listOfCyclicPrimes.append(cyclicNumber)
    print ("The list of cyclic primes below or equal to %d is %s, and the number of such primes is %d"%(calculate_upto, sorted(listOfCyclicPrimes), len(listOfCyclicPrimes)))
