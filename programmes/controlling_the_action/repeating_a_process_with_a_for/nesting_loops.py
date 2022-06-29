#Nesting loops
#outter loop
for outer in ["First", "Second", "Third"]:
    print(outer)
    #inner
    for inner in range(3):
        print(inner + 1)
print("Both loops done!")