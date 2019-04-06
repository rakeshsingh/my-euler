#!/usr/bin/python
def read_number():
    number = []
    with open('data/013_number.txt') as datafile:
        for line in datafile:
            number.append(int(line))
            # print(line)
    return number


if __name__ == '__main__':
    number = read_number()
    result = 0
    print(len(number))
    for i in range(len(number)):
        result = result + number[i]

    print(result)
