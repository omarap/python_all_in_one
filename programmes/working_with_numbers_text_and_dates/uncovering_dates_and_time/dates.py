"""
datetime.date is ideal for working with date when time is not an issue

"""
#import datetime module, nickname dt
import datetime as dt

#store today's date in a variable named today
today = dt.date.today()

#store some other date in a variable named last_of_teens
last_of_teens = dt.date(2021, 4, 1)

#output
print(today)
print(last_of_teens)

#you can isolate any part of the date object 
#by using .day, .month, .year.
print(last_of_teens.month)
print(last_of_teens.year)
print(last_of_teens.day)

print(today.day)
print(today.month)
print(today.year)

#formatting strings for dates and time
"""
%a  weekend, abreviated,                        Sun
%A  weekend, Full                               Sunday
%w  weekday number 0-6, where 0 is sunday       0
%d  day number of the month 0-31                31
%b  month name abbreviated                      jan
%B  month name full                             January
%m  month number 01-12                           01
%y  year without century                         19
%Y  year with century                            2019
%H  Hour 0-23                                     23
%I  hour 0-12                                     11
%p  AM/PM                                         PM
%M  Minute 0-59                                   01
%s  Second 0-59                                   01
%f  Microsecond 00000-99999                       495846
%z  UTC offset                                    -0500
%Z  Timezone                                       EST
%j  day number of the year 001-366                 300
%U  Week number of the year                        50
%c  local version of time and date                 Tue Dec 31 23:59:59 2018
%x  local version of time                           23:59:59
%x  local version of date                           12/31/18
%%  A% Character                                    %

"""

print(f"{last_of_teens:%A, %B %d, %Y}")

#date in mm/dd/yyyy format, use %m/%d/%Y
todays_date = (f"{today:%m/%d/%Y}")
print(todays_date)

#Sample date format strings
"""
%a, %b %d %y            Sat, jun 01 2019
%x                      06/01/19
%m-%d-%y                06-01-19
This %A %B %d           This Saturday June 01
%A %B %d is %j of %Y    Saturday June is 152 of 2019
"""