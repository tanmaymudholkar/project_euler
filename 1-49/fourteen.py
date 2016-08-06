#!/usr/bin/env python
import numpy
import math

def collatz(n):
    if isinstance(n,(int,long)):
        if(n>0):
            if(n%2==0):
                return(int(n/2))
            else:
                return(int(3*n+1))
        else:
            print "nonsense value"
            quit()

maxcounter=0
for i in range(2,1000000):
    nxt=i
    counter=1
    while True:
        while(nxt!=1):
            nxt=collatz(nxt)
            counter=counter+1
        if(counter>maxcounter):
            imax=i
            maxcounter=counter
        break

print imax
