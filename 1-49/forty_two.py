#!/usr/bin/env python

from __future__ import print_function, division

from peModules.alphabet import indexOfAlphabet
from math import sqrt,ceil

def isPerfectSquare(candidate):
    if candidate == int(round(sqrt(candidate*1.)))*int(round(sqrt(candidate*1.))):
        return True
    return False

def isTriangleNumber(candidate):
    if (isPerfectSquare(1+8*candidate)):
        discriminant = int(round(sqrt(1+8*candidate)))
        if (discriminant-1)%2==0:
            return True
    return False

def calculateScore(word):
    score = 0
    for letter in word:
        lowerLetter = letter.lower()
        score += indexOfAlphabet[lowerLetter]
    return score

if __name__ == "__main__":
    inputFileName = "p042_words.txt"
    inputFile = open(inputFileName)
    counter = 0
    for commaSeparatedListOfWords in inputFile:
        listOfWords = [wordInQuotes.strip("\"") for wordInQuotes in commaSeparatedListOfWords.split(",")]
        for word in listOfWords:
            if (isTriangleNumber(calculateScore(word))):
                print ("%s has a triangle digit score %d"%(word,calculateScore(word)))
                counter += 1
    print ("Number of such words is %d"%(counter))
