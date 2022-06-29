#Multi-key dictionaries
#Example
"""
For example, suppose that just knowing the persons full name isnt enough. You
want to also know the year the person was hired, his or her date of birth, and
whether or not that employee has been issued a company laptop. The dictionary
for any one person might look like this:

"""

employee = {
    'name':'Haru Tanaka',
    'year_hired':2005,
    'dob':'11/23/1987',
    'has_laptop':'False'
}
print(employee)

#Example2
"""
Or suppose you need a dictionary of products that you sell. 
For each product, you want to know its name, its unit price, 
whether or not its taxable, and how many you currently have in stock.

"""
product = {
    'name': 'Ray-Ban WayFarer Sunglasses',
    'unit_price': 112.99,
    'taxable': True,
    'in_stock': 10,
    'models': ['black', 'tortoise']
}
print(product)

#display for value of the data dictionary
#product
print(product['name'])
print(product['unit_price'])
print(product['taxable'])
print(product['models'])
print(product['in_stock'])

#descriptive display of products
print('Name:   ', product['name'] )
print('Price: ', f"$ {product['unit_price']: .2f}")
print('Taxable ', product['taxable'])
print('In Stock  ', product['in_stock'] )
print('Models: ')
for model in product['models']:
    #The " " * 10 on the last line of code 
    # means print a space (“ ”) ten times
    print("  " * 10 ,  model)

#employee
print(employee['dob'])
print(employee['has_laptop'])
print(employee['name'])
print(employee['year_hired'])