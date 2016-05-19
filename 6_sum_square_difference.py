#!/usr/bin/python
from functools import reduce

def sum_squares_difference(n):
    sum_of_squares = reduce(lambda x,y:x+y, map(lambda x: x**2, range(1,n+1)))
    square_of_sums = reduce(lambda x,y:x+y, range(1,n+1)) ** 2
    if square_of_sums > sum_of_squares:
        return square_of_sums - sum_of_squares
    return sum_of_squares - square_of_sums

if __name__ == '__main__':
    print(sum_squares_difference(100))
