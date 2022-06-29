#Nesting dictionaries
"""
        SYNTAX
containigdictionaryname = {
    key:{dictionary},
    key:{dictionary},
    key:{dictionary}
}

"""
products = {
    'RB00111':{'name': 'Roy-Ban Sunglasses', 'price':112.98, 'models':['black', 'tortoise']},
    'DWC0317':{'name': 'Drone with Camera', 'price':72.95, 'models':['white', 'black']},
    'MTS0540':{'name': 'T-shirt', 'price':2.95, 'models':['small', 'medium', 'large']},
    'ECD2989':{'name':'Echo Dot','price':29.299, 'models':[]} 
}

#this header shows above the output
print(f"{'ID':<6} {'Name':<17} {'price':>8} {'models'}")
print('-' * 60) #print 60 hyphens 

#loop through each dictionary in the products dictionary
for one_product in products.keys():
    #get the id of one product
    id = one_product

#get the name of one product
name = products[one_product] ['name']

#get the unit price of one product and format with $
unit_price = '$' + f"{products[one_product]['price']:.2f}"

#create an empty string variable named models
models = ''

#loop through the models list and track onto models
#one item from the list followed by a comma and a space
for m in products[one_product] ['models']:
    models+=m + ' , '
#if the models variable is more than two characters in length
#peel of the last two characters (last comma & space)
if len(models) > 2:
    models = models[:-2]
else:
    models = "<none>"

#print all the variable with a neat f-string
print(f"{id:<6} {name:<17} {unit_price:>8} {models}")