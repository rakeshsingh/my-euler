#!/usr/bin/python
import math
from math import gcd


def my_gcd(a, b):
    '''
    returns: str
    gcd for two given numbers
    '''
    if a == b or b == 0:
        return a
    elif a > b:
        return gcd(a-b, b)
    else:
        return gcd(b-a, a)


def lcm(a, b):
    ''''''
    return a * b // gcd(a, b)


def get_prime_factors(n):
    '''
    returns a list of prime factors of a number
    '''
    factors = []
    for i in get_next_prime(1):
        if n % i == 0:
            factors.append(i)
        if i > n:
            return factors


def is_prime(n):
    '''
    Check whether a number is prime or not
    '''
    if n > 1:
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(n) + 1), 2):
            if n % current == 0:
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


def fibonacci_generator():
    """Fibonacci numbers generator"""
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


def fibonacci(n):
    """
        Fibonacci numbers
        returns: int
    """
    counter = 0
    for fib in fibonacci_generator():
        if counter == n:
            return fib
        counter = counter + 1


def hello():
    print('Hello World !')


if __name__ == '__main__':
    for i in fibonacci_generator():
        print(i)
        if i > 150:
            break
