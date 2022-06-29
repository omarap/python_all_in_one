#Finding a list item's index
#Python offers .index() that returns a position of an item in a list
"""
        SYNTAX
    listname.index(x)

"""
#List of strings
grades = ["C", "B", "A", "D", "C", "B", "C"]

#Find the index for B
b_index  = grades.index("B")

#Output
print(b_index)

#Example2
grades2 = ["C", "B", "A", "D", "C", "B", "C"]

#Decide what to look for
look_for = "F"

#see if the item is in the list
for look_for in grades2:
    #if it's in the list, get and show the item
    print(str(look_for) + " is at index " + str(grades2.index(look_for)))
else:
    #if not in the list
    print(str(look_for)+ " not in the list.")