#Accounting for time zones
#As you know when it is noon in your neighbourhood it doesn't that mean it's noon everywhere
#Working with time zones
import datetime as dt

#import dateutil tz
from dateutil.tz import gettz

#Determing the difference between your time and UTC time

#Get the time from your computer clock
here_now = dt.datetime.now()

#Get the UTC datetime right now
utc_now = dt.datetime.utcnow()

#Substract the difference
time_difference = (utc_now - here_now)

#output
print(time_difference)

#output2
print(f"My time:  {here_now:%I %M %p}")
print(f"UTC time: {utc_now:%I %M %p}")
print(f"Difference:{time_difference}")

#working directly with time zones
#UTC time zone right now
utc = dt.datetime.now(gettz('Etc/UTC'))
print(f"utc:{utc:%A %D %I:%M %p %Z}")

#USA Eastern time
est = dt.datetime.now(gettz('America/New york'))
print(f"est:{est:%A %D %I:%M %p %Z}")

#USA Central time
cst = dt.datetime.now(gettz('America/Chicago'))
print(f"cst:{cst:%A %D %I:%M %p %Z}")

#USA Mountain time
mst = dt.datetime.now(gettz('America/Boise'))
print(f"mst:{mst:%A %D %I %p %Z}")

pst = dt.datetime.now(gettz('America/Los_Angeles'))
print(f"pst:{pst:%A %D %I %p %Z}")

#Date and time for a scheduled event in multiple time zones
# event = dt.datetime(2020, 7 , 4, 19, 0, 0)

#July 4 Event 7:00 locatime
event = dt.datetime(2020, 7, 4, 19, 0, 0)

#local date and time
print("Local:" + f"Event: {event:%D %I:%M %p %Z}")

event_eastern = event.astimezone(gettz('America/New_york'))
print(f"event:{event_eastern: %D %I:%M %p %Z}")

event_central = event.astimezone(gettz('America/Chicago'))
print(f"event:{event_central: %D %I:%M %p %Z}")

event_mountain = event.astimezone(gettz('America/Denver'))
print(f"event:{event_mountain:%D %I:%M %p %Z}")

event_pacific = event.astimezone(gettz('America/Los_Angeles'))
print(f"event:{event_pacific:%D %I:%M %p %Z}")

event_utc = event.astimezone(gettz('Etc/UTC'))
print(f"event:{event_utc:%D %I:%M %p %Z}")
