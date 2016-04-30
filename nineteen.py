#!/usr/bin/env python

from __future__ import print_function
from __future__ import division

def isLeapYear(year):
    if (year%400==0):
        return True
    else:
        if(year%100==0):
            return False
        else:
            if(year%4==0):
                return True
            else:
                return False

def increment():
    global day,month,year
    if (day < 28):
        day += 1
    else:
        if (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
            if (day < 31):
                day += 1
            else:
                day=1
                if (month == 12):
                    month=1
                    year += 1
                else:
                    month += 1
        elif (month==4 or month==6 or month==9 or month==11):
            if (day < 30):
                day += 1
            else:
                month += 1
                day=1
        else:
            if (day==28):
                if (isLeapYear(year)):
                    day += 1
                else:
                    month += 1
                    day=1
            else:
                month += 1
                day=1

if __name__=="__main__":
    weekday=1 # 0 = Sunday, 1 = Monday etc.
    day=1
    month=1 # 1=Jan, 2=Feb etc.
    year=1900
    counter = 0
    # while (not(year==1902 and month==1 and day==31)):
    while (not(year==2000 and month==12 and day==31)):
        increment()
        weekday += 1
        weekday = weekday%7
        print ("%d/%d/%d was a %s"%(day,month,year,"Sunday" if weekday==0 else ("Monday" if weekday==1 else ("Tuesday" if weekday==2 else ("Wednesday" if weekday==3 else ("Thursday" if weekday==4 else ("Friday" if weekday==5 else ("Saturday" if weekday==6 else ("Unknown weekday")))))))))
        if (day==1 and weekday==0):
            # print ("%d/%d/%d was a Sunday"%(day,month,year))
            if (year >= 1901):
                counter += 1

    print ("Number of firsts of the month coinciding with Sundays = %d"%(counter))
