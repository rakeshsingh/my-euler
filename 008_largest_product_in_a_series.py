#!/usr/bin/python
from functools import reduce

def read_number():
    number =[]
    with open('data/008_number.txt') as datafile:
        for line in datafile:
            for digit in line.strip():
                number.append(int(digit))
            #print(line)
    return number

def largest_adjacent_product(number,n):
    product = 0
    for i in range(0,len(number)-n):
        temp_product=reduce(lambda x,y:x*y,number[i:i+n])
        if temp_product > product:
            product = temp_product
    return product

if __name__=='__main__':
    #print(len(read_number()))
    print(largest_adjacent_product(read_number(),13))