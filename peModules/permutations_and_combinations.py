from __future__ import print_function, division

def listCyclicPermutationGenerator(sourceList):
    if (not(isinstance(sourceList,list))):
        raise TypeError('Input not a list?')
    if (len(sourceList) <= 1):
        raise ValueError('List not long enough to permute cyclically')
    
    yield sourceList
    number_of_permutations_required = len(sourceList)-1
    currentList = sourceList
    for permutations_counter in range(0,number_of_permutations_required):
        lastElement = currentList.pop(-1)
        currentList.insert(0, lastElement)
        yield currentList

def listPermutations(sourceList):
    if (not(isinstance(sourceList,list))):
        raise TypeError('Input not a list?')
    if (len(set(sourceList)) != len(sourceList)):
        raise TypeError('Input list has at least one repeated element?')
    if (len(sourceList) == 0):
        yield []

    for sourceIndex in range(len(sourceList)):
        newList = [element for element in sourceList]
        sourceElement = newList.pop(sourceIndex)
        for newPermutation in listPermutations(newList):
            yield [sourceElement] + newPermutation
