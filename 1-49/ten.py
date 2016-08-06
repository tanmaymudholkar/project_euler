#!/usr/bin/env python
import numpy
import math

def is_prime(n):
    if(n<2 or not isinstance(n,(int,long))):
        print "nonsensical input"
        quit()
    if ((n%2==0 or n%3==0) and (n!=2 and n!=3)):
        return False
    for i in range (5,1+int(math.floor(math.sqrt(n))),6):
        if (n%i==0 or n%(i+2)==0):
            return False
    return True

sum=0
for i in range (2,2000001):
    if(is_prime(i)):
        print i
        sum=sum+i

print sum
