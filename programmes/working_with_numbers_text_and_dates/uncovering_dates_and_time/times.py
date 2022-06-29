import datetime as dt

#Working with times
#if you want to work strictly with time data use datetime.time class
#basic syntax
#variable = datetime.time(hour,[minute,[second, [macrosecond]]])

#notice how all arguments are optional
midnight = dt.time()
print(midnight)

#get the type of time
print(type(midnight))

#almost_midnight
almost_midnight = dt.time(23,59,59,999999)
print(almost_midnight)

#Sample time formar strings
"""
%I:%M %p                        11:59 PM
%H:%M:%S and %f microseconds    23:59:59 and 999999 microseconds
%X                              23:59:59

"""
#right_now
right_now = dt.datetime.now()
print(right_now)

#you can define datetime using any of the following
#datetime(year, month, day, hour, [minute, [microsecond]])
#Here is an example using 11:59 PM on December 31 2019:
new_years_eve = dt.datetime(2019, 12, 31, 23,  59, 59)
print(new_years_eve)

