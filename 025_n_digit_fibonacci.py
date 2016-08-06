#!/usr/bin/python
from euler.utils import fibonacci_generator

def get_index_of_n_digit_fibonacci(n):
    ''' 
    This function returns the first index of
    N digit fibonacci number
    '''
    index = 0
    for p in fibonacci_generator():
        index = index + 1
        if(len(str(p))) == n:
            print(p)
            break
    return index

if __name__ == '__main__':
    print(get_index_of_n_digit_fibonacci(1000))