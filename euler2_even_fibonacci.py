#!/usr/bin/python

def nth_fibonacci(n):
    if n > 0 and n<= 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def sum_of_even_fibonacci(n):
	sum = 0
	previous=1
	current =2 
	while current <n:
	    if current%2 ==0:
	        print('{} is even'.format(current))
	        sum = sum + current
	    current = current + previous
	    previous = current - previous
	return sum


if __name__ == '__main__':
	print(sum_of_even_fibonacci(4000000))
