#Getting dictionary data with get().
"""
            SYNTAX
    dictionaryname.get(key)

"""
#Make a dictionary named people
people = {
    'htanaka': 'Haru Tanaka',
    'ppatel': 'Priya Patel',
    'bagarcia': 'Benjamin Alberto Garcia',
    'zmin': 'Zhang Min',
    'afarooqi': 'Ayesha Farooqi',
    'hajackson': 'Hanna Jackson',
    'papatel': 'Pratyush Aarav Patel',
    'hrjackson': 'Henry Jackson'
 }

#Look for a person
person = "bagarcia"
print(people.get(person))

#Example2 
person = "schmeedledorp"
print(people.get(person))

#Example3
print(people.get('schmeedledorp', 'unknown person to this dictionary'))