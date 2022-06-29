#The pop method offers another method to remove data from dictionaries
#Example
#Define a dictionary called people
people = {
    'htanaka':'Haru Tanaka',
    'zmin': 'Zhang  Min',
    'afarooqi':'Ayesha Farooqi'
}

#show the original people dictionary
print(people)

#pop zmin from the dictionary, store it's value in adios variable
adios = people.pop('zmin')

#print the contents of people and adios
print(people)
print(adios)

