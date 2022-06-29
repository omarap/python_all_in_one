#Data dictionaries offers a variation in pop that uses this syntax
# dictionaryname = popitem()
#Define a dictionary called people
people = {
    'htanaka':'Haru Tanaka',
    'zmin': 'Zhang  Min',
    'afarooqi':'Ayesha Farooqi'
}

#popitem() example
adios = people.popitem()

#output
print(people)
print(adios)