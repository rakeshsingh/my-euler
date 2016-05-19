#!/usr/bin/python
from euler.utils import get_primes

if __name__ == '__main__':
    counter=0
    for prime in get_primes(1):
        counter = counter+1
        if counter==10001:
            print(prime)
            break
