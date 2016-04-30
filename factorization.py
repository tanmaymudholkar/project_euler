#!/usr/bin/env python

from __future__ import print_function
from __future__ import division

import numpy
import math

class prime_factorization:
    def __init__(self,a,b):
        self.primefactors=a
        self.exponents=b
        expded=numpy.array([],dtype=int)
        for i in range(0,a.size):
            for j in range(0,b[i]):
                expded=numpy.append(expded,a[i])
        self.expanded=expded
                
    def prnt(self):
        print ("Prime factors: %s"%(self.primefactors))
        print ("Exponents: %s"%(self.exponents))
        print ("Expanded: %s"%(self.expanded))

def prime_factors(n):
    m=n
    if(isinstance(n,(int,long))):
        factors=numpy.array([],dtype=int)
        expos=numpy.array([],dtype=int)
        for i in range(2,1+int(math.floor(math.sqrt(n)))):
            if(m%i==0):
                factors=numpy.concatenate((factors,numpy.array([i],dtype=int)))
                counter=0
                while(m%i==0):
                    counter=counter+1
                    m=m/i
                expos=numpy.concatenate((expos,numpy.array([counter],dtype=int)))
        if(m==1):
            to_return=prime_factorization(factors,expos)
        else:
            factors=numpy.concatenate((factors,numpy.array([m],dtype=int)))
            expos=numpy.concatenate((expos,numpy.array([1],dtype=int)))
            to_return=prime_factorization(factors,expos)
        return to_return
    else:
        print ("nonintegral value")
        quit()

def proper_divisors(n):
    limit_up_to_which_to_check = n//2
    list_of_proper_divisors = numpy.array([], dtype=int)
    for putative_factor in range(1,1+limit_up_to_which_to_check):
        if (n%putative_factor == 0):
            list_of_proper_divisors=numpy.concatenate((list_of_proper_divisors,numpy.array([putative_factor],dtype=int)))
    return list_of_proper_divisors

def all_factors(n):
    list_of_proper_divisors = proper_divisors(n)
    list_of_factors=numpy.concatenate((list_of_proper_divisors,numpy.array([n],dtype=int)))
    return list_of_factors
