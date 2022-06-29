#python offers a sort() method for sorting lists
"""
        SYNTAX
    lastname.sort()

"""
#Sorting strings and numbers
#Create a list of strings
names = ["Zara", "Lupe", "Hong", "Alberto", "Jake", "Tyler"]

#Create a list of numbers
numbers = [14, 0 , 56, -4, 99, 56, 11.23]

#sort the names list
names.sort()
#sort the numbers list
numbers.sort()

names.sort(key=lambda s: s.lower())
print(names)

#show the results
print(names)
print(numbers)

