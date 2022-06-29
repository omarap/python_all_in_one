#Bailing out of a loop
"""
            SYNTAX
    for x in items:
        if condition:
            [do this]
            break
    do this
"""
#Example
answers = ["A", "C", "B", "D"]
for answer in answers:
    if answer == " ":
        print ("Incomplete")
        break
    print(answer)
print("Done!")

#Example2
answers = ["A", "C", "", "D"]
for answer in answers:
    if answer == "":
        print("Incomplete !")
        break
    print(answer)
print("All done !")