#Returning values from functions
def alphabetize(original_list=[]):
    """
    pass any list in square brackets, 
    a string with items sorted

    """
    #inside the function make a copy of the list passed in
    sorted_list = original_list.copy()

    #sort the working copy
    sorted_list.sort()

    #make a new empty string for the output
    final_list = ''
    
    #loop throught the list and append name, comma and space
    for name in sorted_list:
        final_list += name + ', '

    #knock out the last comma space
    final_list = final_list[:-2]

    #return the alphatized list
    return final_list

random_list = ['McMullen', 'Keaser', 'Maier', 'Wilson', 'Yudt', 'Gallagher',
'Jacobs']
alpha_list = alphabetize(random_list)
print(alpha_list)