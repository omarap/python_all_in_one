#using the mysterious fromkeys() and setdefault methods

"""
            fromkeys method syntax
newdictionaryname = dict.fromkeys(iterable, [value])

"""
#Example
DWC001 = dict.fromkeys(['name', 'unit_price', 'taxable', 'in_stock', 'models'])
print(DWC001)

#create a generic dictionary of products named product
product ={
    'name':'',
    'unit_price': 0,
    'taxable': True,
    'in_stock': 0,
    'models': []
}

#create a dictionary named DWC001 that has the same name as products
DWC001 = dict.fromkeys(product.keys())

#show what is in the new dictionary
print(DWC001)

"""
the .setdefault() value lets you add a new key to a dictionary 
with predefined values.
"""

#Example
"""
An example in which we created the DWC001 dictionary
using the same keys as the product dictionary. 
After the dictionary is created,
setdefault('taxable', True) adds a key named taxable and 
sets its value to True — but only if that dictionary 
doesnt already have a key named taxable.
It also adds a key named reorder_point and sets its value to 10 but, 
again, only if that key doesnt already exist.
"""
#Experimenting with fromkeys and setdefault.
#create a generic dictionary for products named product
product = {
    'name':'',
    'unit_price': 0,
    'taxable': True,
    'in_stock': 0,
    'models': []
}

#create a dictionary for product SKU #DWC001
DWC001 = dict.fromkeys(product.keys())
DWC001.setdefault('taxable', True)
DWC001.setdefault('models', [])
DWC001.setdefault('re_order_point', 100)

#show what's in the new dictionary
print("Dictionary after fromkeys() and setdefault()")
print(DWC001)

#change the taxable field from none to True
print("Dictionary after fromkeys() and setdefault()")
DWC001['taxable'] = True

#print the dictionary after changing taxable to True
print(DWC001)