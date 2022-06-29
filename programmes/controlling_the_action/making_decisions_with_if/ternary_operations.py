age = 31
if age < 21:
    # if under 21, no alcohol
    beverage = "milk"
elif age >= 21 and age < 80:
    #ages 21 - 79, suggest beer
    beverage = "beer"
else:
    # if 80 or older, prune juice be a good juice
    beverage = "Prune juice"
print("Have a " + beverage)
