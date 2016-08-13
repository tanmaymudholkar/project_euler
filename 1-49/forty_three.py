#!/usr/bin/env python

from __future__ import print_function, division

from sys import exit

requiredPandigitals = []
currentIndexToDivisibilityCheck = {2:2, 3:3, 4:5, 5:7, 6:11, 7:13}

def generateLastThree():
    multiplier = 1
    product = 1
    while True:
        product = 17*multiplier
        multiplier += 1
        if (product > 1000):
            break
        candidateStr = str(product)
        if (product < 100):
            candidateStr = "0"+candidateStr
        if (len(candidateStr) == len(set(list(candidateStr)))):
            yield candidateStr

def populateRequiredPandigitals(currentIndex, filledSoFarStr):
    global requiredPandigitals
    if (currentIndex == 1):
        for missingDigit in range(0,10):
            if str(missingDigit) not in filledSoFarStr:
                break
        requiredPandigitals += [int(str(missingDigit)+filledSoFarStr)]
    else:
        for candidateExtraDigit in range(0,10):
            if str(candidateExtraDigit) not in filledSoFarStr:
                candidateStr = str(candidateExtraDigit) + filledSoFarStr[:2]
                candidate = int(candidateStr)
                if candidate%currentIndexToDivisibilityCheck[currentIndex] == 0:
                    newFilledSoFarStr = str(candidateExtraDigit) + filledSoFarStr
                    populateRequiredPandigitals(currentIndex-1, newFilledSoFarStr)
                
def startHereRequiredPandigitals():
    for lastThreeStr in generateLastThree():
        listToAvoid = [int(digitStr) for digitStr in lastThreeStr]
        filledSoFarStr = lastThreeStr
        populateRequiredPandigitals(7,filledSoFarStr)

if __name__ == "__main__":
    startHereRequiredPandigitals()
    sumRequired = 0
    for pandigital in requiredPandigitals:
        print ("%d obeys the given properties"%(pandigital))
        sumRequired += pandigital

    print ("sumRequired is %d"%(sumRequired))
