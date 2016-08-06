#!/usr/bin/env python
import numpy
import math

fibo=numpy.array([long(1),long(1)],dtype='uint64')
last_index=fibo.size
imax=100

def fib(n):
    global fibo,last_index
    if (n>0):
        if(n>last_index):
            for i in range(last_index+1,n+1):
                fibo=numpy.concatenate((fibo,numpy.array([fibo[i-2]+fibo[i-3]],dtype='uint64')))
            last_index=fibo.size
        return fibo[n-1]
    else:
        print "Error in index"
        return -1

for i in range (1,imax+1):
    print fib(i)
