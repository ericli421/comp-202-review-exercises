def transpose(initial_list):
    '''
    This function takes in a 2d square list and transposes it by turning 
    rows into columns and vice versa. 

    Parameters:
        initial_list: 2d rectangular list

    Returns: 
        list: the transpose of initial_list

    >>> transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    >>> transpose([[True, False, True],[False, True, False]])
    [[True, False], [False, True], [True, False]]
    >>> transpose([["Hello"]])
    [['Hello']]
    
    '''

    output_list = []

    for i in range(len(initial_list[0])):

        temp_list = []

        for j in range(len(initial_list)):

            temp_list.append(initial_list[j][i])

        output_list.append(temp_list)

    
    return output_list
