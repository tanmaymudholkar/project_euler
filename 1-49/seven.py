#!/usr/bin/env python
import numpy
import math

class factorization:
    def __init__(self,a,b):
        self.primefactors=a
        self.exponents=b
        expded=numpy.array([],dtype=int)
        for i in range(0,a.size):
            for j in range(0,b[i]):
                expded=numpy.append(expded,a[i])
        self.expanded=expded
                
    def prnt(self):
        print self.primefactors
        print self.exponents
        print self.expanded

def factors(n):
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
            to_return=factorization(factors,expos)
        else:
            factors=numpy.concatenate((factors,numpy.array([m],dtype=int)))
            expos=numpy.concatenate((expos,numpy.array([1],dtype=int)))
            to_return=factorization(factors,expos)
        return to_return
    else:
        print "nonintegral value"
        quit()

def is_prime(n):
    facts=factors(n).primefactors
    if (facts[0]==n):
        return True
    else:
        return False

n=2
primes_found=0
while primes_found<10001:
    if (is_prime(n)):
        prime=n
        primes_found=primes_found+1
    n=n+1

print prime
