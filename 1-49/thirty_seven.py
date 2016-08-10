#!/usr/bin/env python

from __future__ import print_function, division

from peModules.primality import is_prime

leftmostDigitsAllowed = [2,3,5,7]
middleDigitsAllowed = [1,3,7,9]
rightmostDigitsAllowed = [3,7]

leftBuildDigits = [leftmostDigit for leftmostDigit in leftmostDigitsAllowed]
for middleDigit in middleDigitsAllowed:
    if middleDigit not in leftBuildDigits:
        leftBuildDigits += [middleDigit]

rightBuildDigits = [rightmostDigit for rightmostDigit in rightmostDigitsAllowed]
for middleDigit in middleDigitsAllowed:
    if middleDigit not in rightBuildDigits:
        rightBuildDigits += [middleDigit]

truncatableList = [[[]],[[]]] # Format: first index = left(0) or right(1), second index = number of digits - 2
directionRepresentationDict = {"left":0, "right":1} # defining format from above

def fillTruncatableList(numberOfDigits, direction):
    global truncatableList
    listOfTruncatables_givenNumberOfDigits = []
    if (numberOfDigits == 2):
        if direction == "left":
            for leftmostDigit in leftBuildDigits:
                for rightmostDigit in rightmostDigitsAllowed:
                    candidate = int(str(leftmostDigit)+str(rightmostDigit))
                    if is_prime(candidate):
                        if candidate not in listOfTruncatables_givenNumberOfDigits:
                            listOfTruncatables_givenNumberOfDigits += [candidate]
        if direction == "right":
            for leftmostDigit in leftmostDigitsAllowed:
                for rightmostDigit in rightBuildDigits:
                    candidate = int(str(leftmostDigit)+str(rightmostDigit))
                    if is_prime(candidate):
                        if candidate not in listOfTruncatables_givenNumberOfDigits:
                            listOfTruncatables_givenNumberOfDigits += [candidate]
    directionRepresentation = directionRepresentationDict[direction]
    if (numberOfDigits >= 3):
        candidateSeeds = truncatableList[directionRepresentation][numberOfDigits - 3]
        for candidateSeed in candidateSeeds:
            candidateSeedStr = str(candidateSeed)
            firstDigit = int(candidateSeedStr[0])
            lastDigit = int(candidateSeedStr[-1])
            if direction == "left":
                if (firstDigit in middleDigitsAllowed):
                    for additionalDigit in leftBuildDigits:
                        candidate = int(str(additionalDigit) + candidateSeedStr)
                        if is_prime(candidate):
                            if candidate not in listOfTruncatables_givenNumberOfDigits:
                                listOfTruncatables_givenNumberOfDigits += [candidate]
            if direction == "right":
                if (lastDigit in middleDigitsAllowed):
                    for additionalDigit in rightBuildDigits:
                        candidate = int(candidateSeedStr + str(additionalDigit))
                        if is_prime(candidate):
                            if candidate not in listOfTruncatables_givenNumberOfDigits:
                                listOfTruncatables_givenNumberOfDigits += [candidate]
    truncatableList[directionRepresentation][numberOfDigits - 2] = listOfTruncatables_givenNumberOfDigits
    truncatableList[directionRepresentation] += [[]]

  
if __name__ == "__main__":
    leftrightTruncatables = []
    bothListsNonEmpty = True
    numberOfDigits = 2
    while (bothListsNonEmpty):
        for direction in ["left","right"]:
            fillTruncatableList(numberOfDigits, direction)
            print ("At number of digits = %d, list of %s truncatables is: %s"%(numberOfDigits, direction, truncatableList[directionRepresentationDict[direction]][numberOfDigits-2]))
            if (len(truncatableList[directionRepresentationDict[direction]][numberOfDigits-2]) == 0):
                bothListsNonEmpty = False
                break
        if (bothListsNonEmpty):
            for candidate in truncatableList[directionRepresentationDict["left"]][numberOfDigits-2]:
                if candidate in truncatableList[directionRepresentationDict["right"]][numberOfDigits-2]:
                    leftrightTruncatables += [candidate]
        numberOfDigits += 1

    print ("List of left and right truncatables is : %s"%(leftrightTruncatables))
    print ("Number of left and right truncatables is : %d"%(len(leftrightTruncatables)))
    requiredSum = 0
    for leftrightTruncatable in leftrightTruncatables:
        requiredSum += leftrightTruncatable
    print ("And their sum is: %d"%(requiredSum))

    
# Graveyard of stupid attempts:
    
# def isTruncatable(candidate, direction):
#     if (not(isinstance(candidate,int))):
#         # print ("%d is not an integer!"%(candidate))
#         exit("trouble brewing")
#     if (direction != "left" and direction != "right"):
#         print ("Asked for truncatibility in unknown direction: %s; ask for left or right"%(direction))
#     # global truncatableList
#     directionRepresentation = directionRepresentationDict[direction]
#     # if (candidate in truncatableList[directionRepresentation]):
#     #     return True
#     if (not(is_prime(candidate))):
#         return False
#     candidateStr = str(candidate)
#     candidateList = list(candidateStr)
#     if (len(candidateList) == 2):
#         # if not(candidate in truncatableList[directionRepresentation]):
#             # print ("Adding %d to the list"%(candidate))
#             # truncatableList[directionRepresentation] += [candidate]
#         return True
#     indexRange = []
#     if (direction=="left"):
#         indexRange = range(1,len(candidateList)-1)
#     elif (direction=="right"):
#         indexRange = list(reversed(range(2,len(candidateList))))
#     for positionIndex in indexRange:
#         toCheckList = []
#         if (direction=="left"):
#             toCheckList = candidateList[positionIndex:]
#         elif (direction=="right"):
#             toCheckList = candidateList[:positionIndex]
#         toCheckStr = ''.join(toCheckList)
#         toCheckInt = int(toCheckStr)
#         if not(is_prime(toCheckInt)):
#             # if not(candidate in truncatableList[directionRepresentation]):
#                 # print ("Adding %d to the list"%(candidate))
#                 # truncatableList[directionRepresentation] += [candidate]
#             return False
#     return True

# def stupidMiddleDigitsGenerator(numberOfMiddleDigits):
#     if (numberOfMiddleDigits == 0):
#         yield ""
#     else:
#         for middleDigit in middleDigitsAllowed:
#             for rest_of_string in stupidMiddleDigitsGenerator(numberOfMiddleDigits - 1):
#                 yield str(middleDigit)+rest_of_string

# def stupidGenerator(numberOfDigits):
#     if (numberOfDigits == 2):
#         for leftmostDigit in leftmostDigitsAllowed:
#             for rightmostDigit in rightmostDigitsAllowed:
#                 candidate = int(str(leftmostDigit)+str(rightmostDigit))
#                 if (isTruncatable(candidate,"left") and isTruncatable(candidate,"right")):
#                     yield candidate
#     elif (numberOfDigits > 2):
#         for leftmostDigit in leftmostDigitsAllowed:
#             for rightmostDigit in rightmostDigitsAllowed:
#                 allowedMiddleStrings = list(set(stupidMiddleDigitsGenerator(numberOfDigits - 2)))
#                 for allowedMiddleString in allowedMiddleStrings:
#                     candidate = int(str(leftmostDigit)+allowedMiddleString+str(rightmostDigit))
#                     if (isTruncatable(candidate,"left") and isTruncatable(candidate,"right")):
#                         yield candidate

# requiredSum = 0
#     print ("Stupid generator:")
#     for stupidNumberOfDigits in range(2,11):
#         for stupidlyGeneratedTruncatable in stupidGenerator(stupidNumberOfDigits):
#             print ("%d is a truncatable prime"%(stupidlyGeneratedTruncatable))
#             requiredSum += stupidlyGeneratedTruncatable
#     print ("And their sum is: %d"%(requiredSum))


# def isTruncatable(candidate, direction):
#     if (not(isinstance(candidate,int))):
#         # print ("%d is not an integer!"%(candidate))
#         exit("trouble brewing")
#     if (direction != "left" and direction != "right"):
#         print ("Asked for truncatibility in unknown direction: %s; ask for left or right"%(direction))
#     # global truncatableList
#     directionRepresentation = directionRepresentationDict[direction]
#     # if (candidate in truncatableList[directionRepresentation]):
#     #     return True
#     if (not(is_prime(candidate))):
#         return False
#     candidateStr = str(candidate)
#     candidateList = list(candidateStr)
#     if (len(candidateList) == 2):
#         # if not(candidate in truncatableList[directionRepresentation]):
#             # print ("Adding %d to the list"%(candidate))
#             # truncatableList[directionRepresentation] += [candidate]
#         return True
#     indexRange = []
#     if (direction=="left"):
#         indexRange = range(1,len(candidateList)-1)
#     elif (direction=="right"):
#         indexRange = list(reversed(range(2,len(candidateList))))
#     for positionIndex in indexRange:
#         toCheckList = []
#         if (direction=="left"):
#             toCheckList = candidateList[positionIndex:]
#         elif (direction=="right"):
#             toCheckList = candidateList[:positionIndex]
#         toCheckStr = ''.join(toCheckList)
#         toCheckInt = int(toCheckStr)
#         if not(is_prime(toCheckInt)):
#             # if not(candidate in truncatableList[directionRepresentation]):
#                 # print ("Adding %d to the list"%(candidate))
#                 # truncatableList[directionRepresentation] += [candidate]
#             return False
#     return True
