#!/usr/bin/python
from myutil import is_prime, get_next_prime

def largest_prime_factor(n):
    if n <=2:
        raise(RuntimeError('number should be greater than 2'))
    else:
        factor = get_next_prime(1)
        while True:
            if is_prime(n):
                return (n) 
            if n % factor == 0:
                n = n // factor
            else:
                factor = get_next_prime(factor)
            largest_factor=factor
    return factor

if __name__ == '__main__':
    print(largest_prime_factor(600851475143))
