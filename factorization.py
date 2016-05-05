from __future__ import print_function, division

import math

class prime_factorization:
    def __init__(self,a,b):
        self.primefactors=a
        self.exponents=b
        expded=[]
        for i in range(0,len(a)):
            for j in range(0,b[i]):
                expded.append(a[i])
        self.expanded=expded
                
    def prnt(self):
        print ("Prime factors: %s"%(self.primefactors))
        print ("Exponents: %s"%(self.exponents))
        print ("Expanded: %s"%(self.expanded))

def prime_factors(n):
    m=n
    if(isinstance(n,(int,long))):
        factors=[]
        expos=[]
        for i in range(2,1+int(math.floor(math.sqrt(n)))):
            if(m%i==0):
                factors.append(i)
                counter=0
                while(m%i==0):
                    counter=counter+1
                    m=m//i
                expos.append(counter)
        if(m != 1):
            factors.append(m)
            expos.append(1)
        return prime_factorization(factors,expos)
    else:
        print ("nonintegral value")
        quit()

def generate_possible_products(index_primefactor, array_prime_factors, array_exponents):
    if (index_primefactor == len(array_prime_factors) - 1):
        for index_exponent in range(0, 1 + array_exponents[index_primefactor]):
            yield array_prime_factors[index_primefactor]**index_exponent
    else:
        for index_exponent in range(0, 1 + array_exponents[index_primefactor]):
            rest_of_products_generated = generate_possible_products(index_primefactor + 1, array_prime_factors, array_exponents)
            for rest_of_products in rest_of_products_generated:
                yield (array_prime_factors[index_primefactor]**index_exponent)*rest_of_products

def all_factors(n):
    list_of_proper_divisors = []
    prime_factorization_of_n = prime_factors(n)
    array_prime_factors = prime_factorization_of_n.primefactors
    array_exponents = prime_factorization_of_n.exponents
    possible_products_generator = generate_possible_products(0, array_prime_factors, array_exponents)
    for product in possible_products_generator:
        list_of_proper_divisors.append(product)
    list_of_proper_divisors.sort()
    return list_of_proper_divisors
    
def proper_divisors(n):
    list_of_proper_divisors = all_factors(n)
    del list_of_proper_divisors[-1]
    return list_of_proper_divisors
