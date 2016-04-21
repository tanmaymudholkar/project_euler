#!/usr/bin/env python
def factorial(n):
    if(isinstance(n,(int,long))):
        if(n>0):
            return n*factorial(n-1)
        elif(n==0):
            return 1
        else:
            print "nonsense value factorial"
            quit()

def nchoosem(n,m):
    return (int(factorial(n)/(factorial(m)*factorial(n-m))))

if __name__=='__main__':
    print nchoosem(40,20)
