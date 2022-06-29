#passing arbitrary number of arguments
def sorter(*args):
    """
    pass in any number of arguments separated by commas
    inside the function, they are treated as tuple named args

    """
    #Create a list from the passed in tuple
    new_list = list(args)

    #sort and show the list
    new_list.sort()
    print(new_list)

sorter(0.001, 100000, -900, 2)
sorter('Apples', 'Bananas', 'Berries', 'Mangoes', 'Straw berries')