from __future__ import print_function, division

def get_number_of_digits(n):
    if (n<1 or not(isinstance(n, int) or isinstance(n,long))):
        raise TypeError('Only positive integers allowed!')
    number_of_digits_so_far = 0
    while (n != 0):
        n //= 10
        number_of_digits_so_far += 1
    return number_of_digits_so_far

def get_list_of_digits(n):
    if (n<1 or not(isinstance(n, int) or isinstance(n,long))):
        raise TypeError('Only positive integers allowed!')
    list_of_digits = []
    while (n != 0):
        list_of_digits.append(n % 10)
        n //= 10
    list_of_digits.reverse()
    return list_of_digits

def get_sum_of_nth_powers(list_of_digits, n):
    sum_of_nth_powers = 0
    for digit in list_of_digits:
        if (n<0 or n>9 or not(isinstance(n, int))):
            raise TypeError('Only positive digits allowed!')
        sum_of_nth_powers += digit**n
    return sum_of_nth_powers

def get_gcd(m, n):
    if (m<0 or not(isinstance(m, int) or isinstance(m,long))):
        raise TypeError('Only positive integers allowed!')
    if (n<0 or not(isinstance(n, int) or isinstance(n,long))):
        raise TypeError('Only positive integers allowed!')
    if (m==0 or n==0):
        return 0
    if (m<n):
        return get_gcd(n, m)
    if (m%n == 0):
        return n
    return get_gcd(n, m%n)

def get_lcm(m, n):
    if (m<1 or not(isinstance(m, int) or isinstance(m,long))):
        raise TypeError('Only positive integers allowed!')
    if (n<1 or not(isinstance(n, int) or isinstance(n,long))):
        raise TypeError('Only positive integers allowed!')
    return (m*n)//get_gcd(m,n)
