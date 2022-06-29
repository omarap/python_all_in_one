#munipulating_strings_with_methods

#syntax
# string.methodname(params)
#Built-in methods for python3 strings
"""
s.capitalize()      returns the first letter capitalized and the rest lowercase
s.count(x, [y, z])  returns the number of times x appears in string. optionally
with y as the starting point and z as the ending point to search the 
portion of the string.
s.find(x, [y, z])   returns the number indicating the first position to x can be found.
                    optionally y and z allow you to limit the search portion in the string.
s.index(x ,[y ,z])  
s.isalpha()         returns True if s is atleast one character long and contains only letters.
                    (a-z) or (A-Z)
s.isdecimal         returns True if s is atleast one character long and 
                    contains only numeric characters (0-9)
s.isprintable       Returns True if X contains only printable characters
s.istitle()         Returns True if string s contains characters and the first letter of 
                    each word is uppercase and the rest lowercase
s.isupper()         Returns True if all letters in the string are uppercase
s.lower()           Returns s with all characters converted to lowercase
s.Istrip()          Returns s with any leading spaces removed
s.replace(x,y)      Returns a copy of s strings with all characters x replaced by y
s.rfind(x ,[y, z])  similar to s.find() but searches backwards from the start of the string.
                    if y and z are provided searches backwards from z to y.
                    returns -1 if string x not found.
s.rindex()          same as s.rfind() but returns an error if the substring isnt found
s.rstrip()          Returns x with any trailing spaces removed
s.strip()           Returns x with leading and trailing spaces removed.
s.swapcase()        Returns string s with uppercase converted to lowercase and
                    lowercase converted to uppercase
s.title()           Returns string s with the first character of every word capitalized and
                    the rest of the characters lowercase
s.upper()           Returns string s with all characters converted to uppercase

"""
#Example
s1= "There is no such word as schmeedledorp"
s2 = "  abc "
s3 = "ABC"

#capitalize the first letter, the rest lowercase
print(s3.capitalize())

#count the number of spaces in s1
print(s1.count(" "))

#find the dot in s4
print(s3.find("."))

#Is s2 all lowercase letters?
print(s2.islower())

#convert 3 to all lowercase
print(s3.lower())

#String leading characters from s2
print(s2.lstrip())

#String trailing characters from s2
print(s2.rstrip())

#String leading and trailing characters from s2
print(s2.strip())

#swap the case of letters in s1
print(s1.swapcase())

#show s1 in title case
print(s1.istitle())

#show s1 uppercase
print(s1.upper())

