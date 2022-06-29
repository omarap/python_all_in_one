#While loop with break
import random
print("Numbers that aren't visible by 5")
counter = 0
while counter < 10:
    #get a random number
    number = random.randint(1, 999)
    #if its even by 5, bail out
    if int(number) / 5 == number / 5:
        break
    print(number)
    counter += 1
print("All done! ")
