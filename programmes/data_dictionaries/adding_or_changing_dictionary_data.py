#Adding or changing dictionary data
"""
               SYNTAX
    dictionaryname.update(key, value)

"""
#Make a dictionary named people
people = {
    'papatel': 'Pratyush Aarav Patel',
    'hrjackson': 'Henry Jackson'
}

#change the value of hrjackson key
people.update({'hrjackson': 'Henriettab Jackson'})
print(people)

#update the dictionary with a new key:value pair
people.update({'wwiggins': 'Wanda Wiggins'})
print(people)

#show what's in the dictionary now
for person in people.keys():
    print(person + " = " + people[person])