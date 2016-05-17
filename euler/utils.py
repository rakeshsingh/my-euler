#!/usr/bin/python
import math

def least_common_multiple(n):
    lcm =1

    return lcm

def highest_common_factor(n):
    hcf=1
    return hcf

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
            n= yield n
        n = n+1
        
if __name__ == '__main__':
    print(get_next_prime(5))
    print(get_next_prime(7))
