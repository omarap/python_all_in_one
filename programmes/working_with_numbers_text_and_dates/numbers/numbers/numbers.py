#Calculating numbers with function
"""
python functions generally have the syntax:

variablename = function_name(param,[param])

"""
# the abs() functions converts negative to positive numbers
x = -4
y = abs(x)


print(x)
print(y)

#some functions accept two or more values
x = 1.234567890987654321000000000000000000000000001
y = round(x, 2)
print(x)
print(y)

#some built-in python functions for numbers
"""
abs(x) returns an abosulte value for x. converts negative numbers to positive numbers
bin (x) returns a string representation of x convertred  into binary
float(x) returns a string representation or a number of x converted into a float
format(x ,y ) returns x formatted according to pattern specified in y.
hex(x) returns a string containning x converted into hexadecimal. prefixed 0x.
int(x) converts x to an integer type
max(x , y, z.....) takes any number of numeric arguments and returns whichever is largest
min(x , y, z.....) takes any number of numeric arguments and returns whichever is smallest
oct(x)              convets x to an octal number. prefixed 0o
round (x, y)        rounds x to y number of decimal points
str(x)              converts x number to a string datatype
type(x)             returns a string containing the datatype of x.

"""
#Example
#proper syntax for using bulit-in python math functions
pi = 3.14159265358979
x = 128
y = 345.67890987
z = -999.999
print(abs(z))
print(int(z))
print(int(abs(z)))
print(round(pi, 4))
print(bin(x))
print(hex(x))
print(oct(x))
print(max(pi, x, y ,z))
print(min(pi, x, y, z))
print(type(pi))
print(type(x))
print(type(y))