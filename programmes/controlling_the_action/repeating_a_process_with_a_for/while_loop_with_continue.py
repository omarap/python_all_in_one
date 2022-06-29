import random
#starting while loops over with continue
print("Odd numbers!")
counter = 0
while counter < 10:
    #get a random number
    number = random.randint(1,999)
    if int(number / 2) == number / 2:
        #if its an even number, don't print it
        continue
    #print odd number
    print(number)
    #increment the loop counter
    counter += 1
print("All loop is done!")