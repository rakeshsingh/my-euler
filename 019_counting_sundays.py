#!/usr/bin/python

base_day=1
base_day_of_week='Monday
base_year=1900
base_month=1
day_num_map={
    'Monday':1,
    'Tuesday':2,
    'Wednesday':3,
    'Thursday':4,
    'Friday':5,
    'Saturday':6,
    'Sunday':7 
    }

def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 ==0 and year % 400 !=0:
            leap = False
    return leap

def first_day_of_month_count(day, start_year, end_year):
    count = 0
    for year in range(start_year, end_year):
        if is_leap(year):

    return count

if __name__ == '__main__':
    print(first_day_of_month_count('Sunday',1901,2000))