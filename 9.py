#!/usr/bin/env python
import numpy
import math

set_of_squares=numpy.array([],dtype=int)
for i in range(1,1001):
    set_of_squares=numpy.append(set_of_squares,i*i)

def is_part_of_triplet(a,b):
    sumsq=a**2+b**2
    if (sumsq in set_of_squares):
        c=int(math.sqrt(sumsq))
        return c
    else:
        return -1

for a in range(1,1000):
    for b in range(a+1,1001):
        c=is_part_of_triplet(a,b)
        if (c>0 and a+b+c==1000):
            print "(",a,",",b,",",c,")"
            print a*b*c
            quit()
            
