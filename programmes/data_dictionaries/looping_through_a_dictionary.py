#Looping through a dictionary
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

#keys in each item
for person in people:
    print(person)

for person in people.keys():
    print(person)

#value for each item
for person in people:
    print(people[person])

for person in people.values():
    print(person)

#you can loop through the keys and 
#values at the same time using the .items()
for key, value in people.items():
    print(key + " "+ value)

for x, y in people.items():
    print(x + " "+ y)

