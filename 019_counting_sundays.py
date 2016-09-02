#!/usr/bin/python

month_days={1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 ==0 and year % 400 !=0:
            leap = False
    return leap

def how_many_sundays(day, start_year, end_year):
    count = 0
    daynum=365
    for year in range(start_year, end_year+1):
        for month in range(1,13):
            day_of_week=(daynum+1)%7
            if day_of_week==0:
                count+=1
            print('First day of year {} and month {} is {}'.format(year, month, day_of_week))
            #print(year,month)
            if month ==2:
                if is_leap(year):
                    daynum+=1
            daynum+=month_days[month]
            #print(daynum)
    return count

if __name__ == '__main__':
    print(how_many_sundays('Sunday',1901,2000))