#!/usr/bin/env python
import numpy
import math

class twoarrays:
    def __init__(self,a,b):
        self.original=a
        self.reversed=b

def digits(n):
    m=n
    dig=numpy.array([],dtype=int)
    digrev=numpy.array([],dtype=int)
    while m>0:
        dig=numpy.insert(dig,0,m%10)
        digrev=numpy.append(digrev,m%10)
        m=m/10
    twoarrs=twoarrays(dig,digrev)
    return twoarrs

def is_pal(n):
    twoarrs=digits(n)
    if((twoarrs.original==twoarrs.reversed).all()):
        return True
    else:
        return False

max=10000
for i in range (100,1000):
    print i
    for j in range (100,1000):
        prod=i*j
        if(is_pal(prod) and prod>max):
            max=prod

print max
