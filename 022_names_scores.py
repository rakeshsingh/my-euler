#!/usr/bin/python

char_vals={
        'A':1,
        'B':2,
        'C':3,
        'D':4,
        'E':5,
        'F':6,
        'G':7,
        'H':8,
        'I':9,
        'J':10,
        'K':11,
        'L':12,
        'M':13,
        'N':14,
        'O':15,
        'P':16,
        'Q':17,
        'R':18,
        'S':19,
        'T':20,
        'U':21,
        'V':22,
        'W':23,
        'X':24,
        'Y':25,
        'Z':26

    }
def names_scores():
    names=[]
    with open('data/p022_names.txt') as datafile:
        for line in datafile:
            print(line.strip())
            for word in line.split(','):
                names.append(word.strip('"'))
    names.sort()
    counter=0
    score=0
    for name in names:
        counter = counter + 1
        print(name)
        worth=0
        for char in name:
            worth = worth + char_vals[char]
        score = score + counter * worth
    print(score)

if __name__=='__main__':
    names_scores()           