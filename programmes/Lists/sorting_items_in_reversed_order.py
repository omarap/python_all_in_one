import datetime as dt

#list of strings
names = ["Zara", "Lupe", "Hong", "Alberto", "Jacky", "Tyler"]

#list of numbers
numbers = [14, 0, 56, -4, 99, 56, 11.3]

#list of dates
datelist = []
datelist.append(dt.date(2020, 12, 31))
datelist.append(dt.date(2019, 1, 31))
datelist.append(dt.date(2018, 2, 28))
datelist.append(dt.date(2020, 1, 1))

#sorting lists in reversed order (Z to A)
names.sort(reverse=True)
print(names)
print()

#Sort the dates in reversed order, (latest to earliest)
datelist.sort(reverse=True)
for date in datelist:
    print(f"date:{date:%m/%d/%Y}")