#!/usr/bin/env python
import numpy
import math

# fibo=numpy.array([1,1])
# last_index=fibo.size

def fib(n):
    # global fibo,last_index
    # if (n>0):
    #     if(n>last_index):
    #         for i in range(last_index+1,n+1):
    #             fibo=numpy.concatenate((fibo,numpy.array([fibo[i-2]+fibo[i-3]])))
    #         last_index=fibo.size
    #     return fibo[n-1]
    # else:
    #     print "Error in index"
    #     return -1
    if(n>0):
        if(n>2):
            return fib(n-1)+fib(n-2)
        elif(n==2):
            return 1
        elif(n==1):
            return 1
    else:
        print "Error in index"
        return -1

# while True:
#     counter=3
#     if(counter>runninglength):
#     current_val=fib

for i in range(1,80):
    print fib(i)
