def list2string(initial_list):
    """
    This function takes as input a 2d list of characters.
    It takes each character from left to right, up to down, and
    forms a string out of it, which it returns

    Args:
        initial_list : 2d list of characters

    Returns:
        str: string encoded in the lists
    >>> list2string([['H','e','l'],['l','o','o'],['B','y','e']])
    'HellooBye'
    >>> list2string([['H','a'],['H','a']])
    'HaHa'
    >>> list2string([['I'],['l','o','v','e'],['I','c','e'],['C','r','e','a','m']])
    'IloveIceCream'
    """
    final_string = ''

    #Adding characters of list to temporary string
    for i in range(len(initial_list)):
        for j in range (len(initial_list[i])):
            final_string = final_string + initial_list[i][j]

    return final_string