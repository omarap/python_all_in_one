#Counting how many times an item appears in the list
"""
        SYNTAX
    listname.count(x)
"""
#Counting items in a list
#Create a list of strings
grades = ["C", "B", "A", "D", "C", "B", "C"]

#count the B's
b_grades = grades.count("B")

#Use a variabel for a value to count
look_for = "C"
c_grades = grades.count(look_for)

print("There are " + str(b_grades)+ " B grades in the list")
print("There are " + str(c_grades) + " " + look_for + "grades in the list")

#Count Fs too
print("There are " + str(grades.count("F")) + " F grades in the list.")