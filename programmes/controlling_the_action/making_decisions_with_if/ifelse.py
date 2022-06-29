import datetime as dt

from sympy import li
"""
            if-else SYNTAX
if condition:
    do indented lines here
else:
    do indented lines here
do the remainig unindented lines no matter what

"""
#An initial greeting based on the time of the day
#Get the current date and time
now = dt.datetime.now()

#make a decision based on hour
if now.hour < 12:
    print("Good morning!")
else:
    print("Good afternoon !")
print("I hope you're doing well!")

#Handling multiple else statements with if
"""
SYNTAX of an if with elif and else
if condition:
    do this indented line
elif:
    do this indented line
do this unidented line no matter what

"""
#Example
light_color = "green"
if light_color == "green":
    print("Go!")
elif light_color == "red":
    print("stop!")
print("this code executes no matter what!")

#if you change the color to red
light_color = "red"
if light_color =="green":
    print("Go!")
elif light_color == "red":
    print("Stop!")
print("This code executes no matter what! ")

#Example3
light_color = "yellow"
if light_color == "green":
    print("Go!")
elif light_color == "red":
    print("Stop!")
print("This code executes no matter what")

#Example4
light_color = "yellow"
if light_color == "green":
    print("Go!")
elif light_color == "red":
    print("stop!")
else:
    print("proceed with precautions! ")
print("this code executes no matter what!")