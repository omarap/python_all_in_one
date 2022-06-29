#Deleting dictionary items
"""
        SYNTAX
    del dictionaryname[key]

"""
#Example
#Define a dictionary called people
people = {
    'htanaka':'Haru Tanaka',
    'zmin': 'Zhang  Min',
    'afarooqi':'Ayesha Farooqi'
}

#show the original people dictionary
print(people)

#remove zmin from the dictionary
del people['zmin']

#show what's in people now
print(people)