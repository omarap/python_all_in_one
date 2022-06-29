#Adding an item at the end of a list or appending
#Create a list of string names
students = ["Mark", "Amber", "Todd", "Anita", "Sunday"]

#Add or append the name Goober to the list
students.append("Goober")

#Add or append new student to the list
new_student = "Amanda"
students.append(new_student)

#Print the entire list
print(students)

#Example_2
student_name = "Cabs"

#Add student name only if not already in the list
if student_name in students:
    print(student_name + '  Already exists')
else:
    students.append(student_name)
    print(student_name + '  added to the list')
print(students)