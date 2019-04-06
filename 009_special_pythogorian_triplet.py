#!/usr/bin/python

'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

from math import sqrt


def special_pythogorian_triplet():
    a = 0
    b = 1
    c = 2
    for a in range(0, 998):
        for b in range(a, 1000 - a):
            c = sqrt(a * a + b * b)
            if c > a and c > b and (a + b + c) == 1000:
                break
        if c > a and c > b and (a + b + c) == 1000:
            break
    # print(a*a, b*b, int(c*c), a*a + b*b)
    # print(a, b, int(c))
    return int(a * b * c)


if __name__ == '__main__':
    # print(len(read_number()))
    print(special_pythogorian_triplet())
