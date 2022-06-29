#passing multiple values in a list
def alphabetize(original_list=[]):
    """
    pass any list in square brackets, display the list
    with items sorted
    """
    #inside the function make a working copy of the passed in list
    sorted_list = original_list.copy()

    #sort the workingcopy
    sorted_list.sort()

    #make a new empty string for the output
    final_list = ''

    #loop through the list, append name, comma and space
    for name in sorted_list:
        final_list += name + ' ,'
    #knock out the last comma space if string is not blank
    final_list = final_list[:-2]

    #print the alphabetized list
    print(final_list)

alphabetize(['Schrepfer', 'Maier', 'Santiago','Adams'])

names = ["Nancy", "Patrick", "Cabaye", "Santiago"]
alphabetize(names)