#Data dictionary methods
"""
clear() empties the dictionary by removing all keys and values
copy() returns a copy of the dictionary
fromkeys() returns a new copy of the dictionary 
but with only specified keys and values.
get() returns the value of the specified key or none if it doesn't exist
keys() returns a list of all keys in the dictionary
pop() removes the item specified in a key from the dictionary and returns its value
popitem() removes the last key value pair.
setdefault() returns the value of the specified key. if key doesn't exist 
it insert the key in the dictionary with specified value.
update() updates the value of an existingkey, or adds a 
new key-value pair if the specified value doesn't exist
values() returns a list of all values in the dictionary

"""
#Copying a dictionary
"""
    SYNTAX
    newdictionaryname = dictionaryname.copy()
"""
#Example
#Define a dictionary called people
people = {
    'htanaka':'Haru Tanaka',
    'zmin': 'Zhang  Min',
    'afarooqi':'Ayesha Farooqi'
}

#Make a copy of the people's dictionary and put it into peeps2
peeps_2 = people.copy()

#Show what is in both dictionaries
print(people)
print(peeps_2)

#to remove all key-value pairs from the dictionary
"""
        SYNTAX
dictionaryname.clear()

"""
#Example
#Remove all data from the dictionary
people.clear()

#show what's in people now
print(people)
