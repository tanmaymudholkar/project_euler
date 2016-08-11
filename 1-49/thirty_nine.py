#!/usr/bin/env python

from __future__ import print_function, division
from math import ceil, sqrt


def getListOfSolutions(perimeter):
    listOfSolutions = []
    upperLimit = int(ceil(perimeter/(2+sqrt(2))))
    for shortestSide in range(1,upperLimit):
        if (perimeter*(perimeter-2*shortestSide))%(2*(perimeter-shortestSide)) == 0:
            longerSide = (perimeter*(perimeter-2*shortestSide))//(2*(perimeter-shortestSide))
            hypotenuse = perimeter - shortestSide - longerSide
            listOfSolutions += [[shortestSide, longerSide, hypotenuse]]
    return listOfSolutions

if __name__ == "__main__":
    maximalNumberOfSolutions = 0
    perimeterAtMaximalNumberOfSolutions = 0
    maximalSolutionsList = []
    for perimeter in range(5,1001):
        solutions = getListOfSolutions(perimeter)
        numberOfSolutions = len(solutions)
        if (numberOfSolutions > maximalNumberOfSolutions):
            maximalNumberOfSolutions = numberOfSolutions
            perimeterAtMaximalNumberOfSolutions = perimeter
            maximalSolutionsList = solutions

    print ("Maximal number of solutions, %d, occurs for perimeter = %d and the list of solutions is %s"%(maximalNumberOfSolutions, perimeterAtMaximalNumberOfSolutions, maximalSolutionsList))
