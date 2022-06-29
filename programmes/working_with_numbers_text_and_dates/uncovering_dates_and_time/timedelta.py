import datetime as dt
#the delta time happens automatically 
#when you substract one date from the other to get the time between

#you can define any timedelta(duration) using this syntax
#datetime.timedelta
#(days= , 
# seconds=, 
# microseconds=, 
# miniseconds=, 
# minutes=,
# hours=,
# weeks=)

#timedelta between
new_years_day = dt.date(2019, 1, 1)
duration = dt.timedelta(days= 146)
print(new_years_day + duration)

#ofcourse you can subtract too, if you start a date of 5/27/2019 and substract
#146 days from it you get 1/1/2019
memorial_day = dt.date(2019, 5, 27)
duration = dt.timedelta(days=146)
print(memorial_day - duration)

#time
start_time = dt.datetime(2019, 3, 31, 8, 0, 0)
finish_time = dt.datetime(2019, 3, 31, 14, 34 , 25)
time_between = finish_time - start_time
print(time_between)
print(type(time_between))

#Example using datetimes with different dates
now = dt.datetime.now()
birthdatetime = dt.datetime(1995, 3, 31, 8, 26)
age = now - birthdatetime
print(age)
print(type(age))

#trying to determine someone's age
today = dt.datetime.now()
birthdate = dt.datetime(2000, 12, 31)
delta_age = today - birthdate
print(delta_age)

#days old
days_old = delta_age.days
print(days_old, type(days_old))

#years old
years_old = days_old / 365
print(years_old)


