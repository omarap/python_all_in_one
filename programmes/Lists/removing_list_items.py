#Removing list items
#Python offers a remove method so that you can remove any items 
#from a list

#Create a list of strings
letters =["A", "B", "C", "D", "C", "E", "C"]

#Remove C from the list
letters.remove("C")

#Show me the new list
print(letters)

#To remove all Cs from the list
while "C" in letters:
    letters.remove("C")
print(letters)

#Another list of letters
letters = ["A", "B", "C", "D", "E", "F", "G"]

#remove the firt_item
letters.pop(0)

#remove the last_item
letters.pop()

#show me the new list
print(letters)

#first_removed
first_removed = letters.pop(0)

#last_removed
last_removed = letters.pop()

#print list
print(letters)

#print first_removed and last_removed from the list
print(first_removed + " and " + last_removed + 
" were removed from the list." )


