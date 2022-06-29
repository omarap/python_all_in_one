#Example
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

#count the number of key:value pairs and put in a variable
howmany = len(people)

#show how many
print(howmany)

"""
Seeing whether a key exists in a dictionary
you can use the in keyboard to see whether a key exists.

if the key exists, it returns True. 
if the key doesn't exists, it returns False

"""
#Is there hajackson in the people dictionary?
print('hajackson' in people)

#Is there schmeedledorp in the people dictionary?
print('schmeedledorp' in people)