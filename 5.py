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

def lcm(i,j):
    factors_i=factors(i).expanded
    factors_j=factors(j).expanded
    common_factors=numpy.array([1],dtype=int)
    while (factors_i.size>0):
        if (factors_i[0] in factors_j):
            common_factors=numpy.append(common_factors,factors_i[0])
            whereitis=numpy.where(factors_j==factors_i[0])[0][0]
            factors_j=numpy.delete(factors_j,whereitis)
        factors_i=numpy.delete(factors_i,0)
    hcf=1
    for cfactor in common_factors:
        hcf=hcf*cfactor
    l=i*j/hcf
    return l

running_lcm=1
for i in range(1,21):
    running_lcm=lcm(running_lcm,i)

print running_lcm
