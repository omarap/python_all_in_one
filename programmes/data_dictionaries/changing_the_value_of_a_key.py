#Changing the value of a key
"""
                SYNTAX
    dictionaryname[key] = newvalue;

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

#print hajackson current value
print(people['hajackson'])

#Changing the value associated with a key in a dictionary.
#change the value of hajackson key
people['hajackson'] = "Hanna Jackson-Smith"

#output
print(people)