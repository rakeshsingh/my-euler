#!/usr/bin/python

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
    else:
        return False
        
def get_primes(n):
    while True:
        if is_prime(n):
            yield n
        n = n+1
        

