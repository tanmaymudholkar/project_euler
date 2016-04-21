#!/usr/bin/env python
import numpy
import math

def factors(n):
    m=n
    if(isinstance(n,(int,long))):
        factors=numpy.array([],dtype=int)
        for i in range(2,int(math.floor(math.sqrt(n)))):
            if(m%i==0):
                factors=numpy.concatenate((factors,numpy.array([i],dtype=int)))
                while(m%i==0):
                    m=m/i
        return factors
    else:
        print "nonintegral value"
        quit()

fac=factors(600851475143)
print fac
