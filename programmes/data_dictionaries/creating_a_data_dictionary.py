#The code for creating a data dictionary follows  this basic syntax
"""
name = {key:value, key:value, key:value, key:value, ...}

"""

#To make a code more readable
"""
name = {
    key:value,
    key:value,
    key:value,
    key:value,....
}

"""
#Example
#Make a dictionary named people
people = {
    'htanaka': 'Haru Tanaka',
    'ppatel': 'Priya Patel',
    'bargarcia': 'Benjamin Alberto Garcia',
    'zmin': 'Zhang Min',
    'hajackson': 'Hanna Jackson',
    'papatel': 'Pratyush Aarav Patel',
    'hrjackson': 'Henry Jackson'
}

#output
print(people)

#Accessing data dictionary
"""
            SYNTAX
        dictionaryname[key]
"""
#For example if you want to know the value of zmin in the dictionary
print(people['zmin'])

#Example2
person  = 'zmin'
print(people[person])

#Example3
person = 'hrjackson'
print(people[person])

#Example4
person = 'schmeedledorp'
print(people[person])