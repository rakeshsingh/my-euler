#!/usr/bin/python
from euler.utils import lcm
from functools import reduce

if __name__ == '__main__':
    print(reduce(lcm, range(1, 11)))
    print(reduce(lcm, range(1, 21)))
