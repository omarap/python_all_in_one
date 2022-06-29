#calculating years old from the timedelta object
import datetime as dt

#Today's date according to your computer
today = dt.date.today()

#Any birth date expressed as year, month, day
birthdate = dt.date(2000, 1, 31)

#Duration between the dates as a time delta
time_delta = today - birthdate

#Duration between the dates as a number (days of)
days_old = time_delta.days

#Floor divide days by 365 to get the number of years
years = days_old // 365

#Days left over is the remainder of days divided by 365.
#floor divide that remainder by 30 for approximate months
months = (days_old % 365) // 30

#print to a format of your liking
print(f"you are {years} years and {months} months old")





