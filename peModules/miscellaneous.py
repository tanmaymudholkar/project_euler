from __future__ import print_function, division

def get_number_of_digits(n):
    if (n<1 or not(isinstance(n, int) or isinstance(n,long))):
        raise TypeError('Only positive integers allowed!')
    number_of_digits_so_far = 0
    while (n != 0):
        n //= 10
        number_of_digits_so_far += 1
    return number_of_digits_so_far

def get_list_of_digits(n):
    # Alternate method: return list(str(n))
    
    if (n<1 or not(isinstance(n, int) or isinstance(n,long))):
        raise TypeError('Only positive integers allowed!')
    list_of_digits = []
    while (n != 0):
        list_of_digits.append(n % 10)
        n //= 10
    list_of_digits.reverse()
    return list_of_digits

def getNumberFromListOfDigits(listOfDigits):
    if (not(isinstance(listOfDigits,list))):
        raise TypeError('Input not a list?')
    resultNumber = 0
    for digit in listOfDigits:
        if (not(isinstance(digit,int))):
            raise TypeError('One element of the list not an int?')
        if (digit < 0 or digit > 9):
            raise ValueError('One of the digits is not between 0 and 9')
        resultNumber *= 10
        resultNumber += digit
    return resultNumber

def get_sum_of_nth_powers(list_of_digits, n):
    sum_of_nth_powers = 0
    for digit in list_of_digits:
        if (n<0 or n>9 or not(isinstance(n, int))):
            raise TypeError('Only positive digits allowed!')
        sum_of_nth_powers += digit**n
    return sum_of_nth_powers

def get_gcd(m, n):
    if (m<0 or not(isinstance(m, int) or isinstance(m,long))):
        raise TypeError('Only positive integers allowed!')
    if (n<0 or not(isinstance(n, int) or isinstance(n,long))):
        raise TypeError('Only positive integers allowed!')
    if (m==0 or n==0):
        return 0
    if (m<n):
        return get_gcd(n, m)
    if (m%n == 0):
        return n
    return get_gcd(n, m%n)

def get_lcm(m, n):
    if (m<1 or not(isinstance(m, int) or isinstance(m,long))):
        raise TypeError('Only positive integers allowed!')
    if (n<1 or not(isinstance(n, int) or isinstance(n,long))):
        raise TypeError('Only positive integers allowed!')
    return (m*n)//get_gcd(m,n)

def isPalindrome(candidateList):
    if (not(isinstance(candidateList,list))):
        raise TypeError('Input not a list?')
    if (len(candidateList) == 0):
        raise ValueError('Palindromicity not defined for empty list!')
    if (len(candidateList) == 1):
        return True
    numElementsToCompare = len(candidateList)//2
    for indexToCompare in range(0, numElementsToCompare):
        if (candidateList[indexToCompare] != candidateList[-indexToCompare-1]):
            return False
    return True

def palindromicNumberGenerator(maxNDigits):
    if not(isinstance(maxNDigits, int)):
        raise TypeError("Max number of digits must be an integer!")
    if (maxNDigits <= 0):
        raise ValueError("Max number of digits must be 1 or higher!")
    for digit_in_middle in range(1,10):
            yield digit_in_middle
    pSeedMax = maxNDigits//2
    if (pSeedMax >= 1):
        for pSeed in range(1,10**(pSeedMax-1)):
            yield int(str(pSeed)+''.join(list(reversed(str(pSeed)))))
            for digit_in_middle in range(0,10):
                yield int(str(pSeed)+str(digit_in_middle)+''.join(list(reversed(str(pSeed)))))
        maxNDigitsEven = (maxNDigits%2 == 0)
        for pSeed in range(10**(pSeedMax-1), 10**(pSeedMax)):
            yield int(str(pSeed)+''.join(list(reversed(str(pSeed)))))
            if (not(maxNDigitsEven)):
                for digit_in_middle in range(0,10):
                    yield int(str(pSeed)+str(digit_in_middle)+''.join(list(reversed(str(pSeed)))))
