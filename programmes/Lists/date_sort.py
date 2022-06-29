import datetime as dt
#Date are little bit trickier coz you have to use the date datatype
#in the list to sort them correctly

#Create a list of dates
dates = [
            dt.date(2020,12, 31), 
            dt.date(2019, 1, 31), 
            dt.date(2018, 2, 28),
            dt.date(2020, 1, 1)
        ]

#Sort the dates
dates.sort()

#output
print(dates)

dates.sort(reverse=True)
print(dates)

#Example2
#Append one date at a time using the dt.date(year, month, day)
#Create a list of dates, empty for starters
datelist = []

#Append the dates one at a time so that the code is easier to read
datelist.append(dt.date(2020, 12, 31))
datelist.append(dt.date(2019, 1, 31))
datelist.append(dt.date(2018, 2, 28))
datelist.append(dt.date(2020, 1, 1))

#sort the dates earliest to latest and show the format
datelist.sort()
for date in datelist:
    print(f"dates:{date:%m/%d/%Y}")