def find_common(l1, l2):
    """
    This function takes as input two lists. It returns
    a list that contains the elements that the two lists share in common

    You can assume each input list does not contain duplicate elements

    Args:
        l1: list
        l2: list

    Returns:
        list: A list that contains the elements the two lists have in common

    >>> find_common([1,2,3], [2,3,4])
    [2, 3]
    >>> find_common([3,4,8,"Hello",False], [5,5,5,"Hi",None])
    []
    >>> find_common([8,7,6,5,4,3,2,1], [1,2,3,4,5,6,7,8])
    [8, 7, 6, 5, 4, 3, 2, 1]
    """
    common_elements = []

    for element in l1:
        
        ### APPROACH 1: Using the in keyword
        # if element in l2:
        #     common_elements.append(element)

        ### APPROACH 2: Using a second for loop
        for compared in l2:
            if element == compared:
                common_elements.append(element)
                continue

    return common_elements

import doctest; doctest.testmod(verbose=True)