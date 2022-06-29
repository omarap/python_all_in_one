#manipulating strings
#concatenating strings
#You can join strings by using a + sign
first_name = "Allan"
middle_init = "C"
last_name = "Simpson"
full_name = first_name + middle_init + last_name
print(full_name)


#Example2
first_name = "Allan"
middle_init = "C"
last_name = "Simpson"
full_name = first_name + " " + middle_init + " " + last_name
print(full_name)

#length of a string
s1 = ""
s2 = " "
s3 = "A B C"
print(len(s1))
print(len(s2))
print(len(s3))

#working with common string operators
"""
python sequence operators that work with strings
x in s          returns True if x exists somewhere in string s
x not in s      returns True if x isnot contained anywhere in string s
s * n or n * s  repeats s n times.
s[i]       The i th item of string s where the first character is zero
s[i:j]      A slice of string x beginning with a character at position i 
            through the character at position j
s[i:j:k]    A slice of s from i to j with step k
min(s)      The smallest (lowest) character in string s.
max(s)      The largest (biggest) character in string s.
s.index(x,[i, [j]]) the first occurence of x in string s.
                    i and j limit the search option from i to j.
s.count(x)      the number of times x appears in larger string s.

"""
#Example
s = "Abracadabra Hocus Pocus you're a turtle dove"

#is there a lowercase t contained in string s
print("t" in s)

#is there an uppercase T contained in string s
print("T" in s)

#print 15 hyphens in a row
print("-" * 15)

#print the first character in string s
print(s[0])

#print characters 33 to 39 from string s
print(s[33:39])

#print any third in string s starting from zero
print(s[0:44:3])

#print lowest character in string s (a space is lower than the letter a)
print(min(s))

#print the highest character in string s
print(max(s))

#where is the first uppercase p
print(s.index("P"))

##########################
print(s.index("o", 22, 44))

#how many lowercase letters are in string s
print(s.count("a"))

#ASCII American Standard Code for Information Interchange