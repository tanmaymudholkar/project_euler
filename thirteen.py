#!/usr/bin/env python
import numpy
import math

class bigint:
    def __init__(self,a):
        self.number=a
    def prnt(self):
        print ''.join(self.number)
    def add(self,toadd):
        a=toadd.number
        b=self.number
        if(len(b)>len(a)):
            for i in range(0,len(b)-len(a)):
                a=['0']+a
        elif(len(a)>len(b)):
            for i in range(0,len(a)-len(b)):
                b=['0']+b

        arev=list(reversed(a))
        brev=list(reversed(b))
        crev=['0']*(len(a)+1)
        for i in range(0,len(a)):
            digit=(int(crev[i])+int(arev[i])+int(brev[i]))%10
            carry=(int(crev[i])+int(arev[i])+int(brev[i]))/10
            crev[i]=str(digit)
            crev[i+1]=str(carry)
        c=list(reversed(crev))
        while(c[0]=='0'):
            c.pop(0)
        bigc=bigint(c)
        return bigc

numbers=open('thirteen.dat','r')

running_sum=bigint(['0'])
tempsum=bigint(['0'])
for line in numbers:
    a=list(str(line).strip())
    biga=bigint(a)
    tempsum=running_sum.add(biga)
    running_sum=tempsum

running_sum.prnt()
print len(running_sum.number)

print
print ''.join(running_sum.number[0:10])
