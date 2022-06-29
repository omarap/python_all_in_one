#Inserting an item into a list
#The insert() method inserts an item in any position of a list
#list_name.insert(position, item)

#Create a list of names
students =["Mark", "Amber", "Todd", "Anita", "Sandy"]

#Add student name to front of a list
student_name = "Lupe"
students.insert(0, student_name)

#Show me the new list
print(students)