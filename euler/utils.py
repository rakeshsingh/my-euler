#!/usr/bin/python
import math
from math import gcd

def my_gcd(a,b):
    if a == b or b ==0:
        return a
    elif a > b:
        return gcd(a-b, b)
    else:
        return gcd(b-a,a)

def lcm(a,b):
    return a*b  // gcd (a, b)

def get_prime_factors(n):
    '''
    returns a list of prime factors of a number
    '''
    factors=[]
    for i in get_next_prime(1):
        if n % i == 0:
            factors.append(i)
        if i >n:
            return factors

def is_prime(n):
    '''
    Check whether a number is prime or not
    '''
    if n >1:
        if n ==2:
            return True
        if n %2 ==0:
            return False
        for current in range(3, int(math.sqrt(n) +1 ),2):
            if n % current ==0:
                return False
        return True
    else:
        return False

def get_next_prime(n):
    while True:
        n = n+1
        if is_prime(n):
            return n

def get_primes(n):
    while True:
        if is_prime(n):
            yield n
        n = n+1

if __name__ == '__main__':
    for i in get_primes(1):
        print(i)
        if i > 100:
            break
