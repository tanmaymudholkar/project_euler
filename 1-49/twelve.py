#!/usr/bin/env python
import numpy
import math

# class factorization:
#     def __init__(self,a,b):
#         self.primefactors=a
#         self.exponents=b
        #expded=numpy.array([],dtype=int)
        #for i in range(0,a.size):
            #for j in range(0,b[i]):
                #expded=numpy.append(expded,a[i])
        #self.expanded=expded
                
    # def prnt(self):
    #     print self.primefactors
    #     print self.exponents
    #     print self.expanded

def factors(n):
    m=n
    if(isinstance(n,(int,long))):
        #factors=numpy.array([],dtype=int)
        expos=numpy.array([],dtype=int)
        for i in range(2,1+int(math.floor(math.sqrt(n)))):
            if(m%i==0):
                #factors=numpy.concatenate((factors,numpy.array([i],dtype=int)))
                counter=0
                while(m%i==0):
                    counter=counter+1
                    m=m/i
                expos=numpy.concatenate((expos,numpy.array([counter],dtype=int)))
        if(m==1):
            to_return=expos
        else:
            #factors=numpy.concatenate((factors,numpy.array([m],dtype=int)))
            expos=numpy.concatenate((expos,numpy.array([1],dtype=int)))
            to_return=expos
        return to_return
    else:
        print "nonintegral value"
        quit()

def factors_ithtri(i):
    ith_triangle=int(i*(i+1)/2)
    if(i%2==0):
        fi=factors(int(i/2))
        fip1=factors(i+1)
    else:
        fi=factors(i)
        fip1=factors(int((i+1)/2))
    factors_i=1
    for j in fi:
        factors_i=factors_i*(j+1)
    factors_ip1=1
    for j in fip1:
        factors_ip1=factors_ip1*(j+1)
    no_of_factors=factors_i*factors_ip1
    return no_of_factors

i=2
no_of_factors=0
while (no_of_factors<500):
    no_of_factors=factors_ithtri(i)
    i=i+1

i=i-1
print (i*(i+1)/2)
