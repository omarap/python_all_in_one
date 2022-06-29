#A tuple is an immutable list. #A tuple can't be modified
#it has data that can't be changed

"""
Consider
Amazon. If we could all go into Amazon and change things at will, 
everything
would cost a penny and wed all have housefuls of Amazon stuff that cost a penny,
rather than housefuls of Amazon stuff that cost more than a penny.

"""

#tuples
prices = (29.95, 9.98, 4.95, 79.98, 2.95)
print(len(prices))

#Count method
print(prices.count(4.95))

#you can use in to see whether a variable exists in a tuple
print(4.45 in prices)

look_for = 12345
if look_for in prices:
    position = prices.index(look_for)
else:
    position = -1
print(position)

#Loop through and display in item in a tuple
for price in prices:
    print(f"$ {price:.2f}")

