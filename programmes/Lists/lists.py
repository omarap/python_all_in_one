#Defining and using lists
#The simplest data collection in python is a list
#A list of test scores
scores = [88, 92, 78, 90, 84]
print(scores)

#A list of students
students =["Mark", "Amber", "Todd", "Anita", "Sandy"]
print(students)

#Referencing list items by position
"""
SYNATX OF referencing a list
        list_name[x]
        
"""
#Referencing list Example
print(students[0])
print(scores[2])
#print the last score in a list of scores
print(scores[4])

#looping through a list
#      SYNTAX
#    for x in list:
#Example
for score in scores:
        print(score)


for score in scores:
        print(score)
        for x in range(1,5):
                print(x)
print("All done!")

#seeing whether a list contains an item