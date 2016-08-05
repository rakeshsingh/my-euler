#!/usr/bin/python
from euler.utils import get_primes
'''
Find the sum of all the primes below two million.
'''

if __name__ == '__main__':
    prime_sum = 0
    for prime in get_primes(1):
        print('current prime number is', prime)
        if prime >=2000000:
            break
        prime_sum = prime_sum + prime
    print(prime_sum)


