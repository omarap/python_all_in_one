#Working with Sets
#Python also offers Sets as means of organising data
#The only difference between a list and a set 
#is that items in a set have no specific order

sample_set ={1.98, 98.9, 74.95, 2.5, 1, 16.3}
print(sample_set)

#Add a single item to a set
sample_set.add(11.23)
print(sample_set)

"""
unlike a list, a set never contains more than one instance of an item

"""

"""
You can add multiple items to a set using the .update() method 
but the items you are adding have to be identified as a list in square brackets
sample_set.update([88, 123.45, 2.98])
print(sample_set)

"""

#You can also copy a set
ss2 = sample_set.copy()
print(ss2)

#length of a set
print(len(sample_set))

#The following displays true if 74.95 in sample_test
print(74.95 in sample_set)

#looping through a set
for price in sample_set:
    print(f"$ {price:>6.2f}")