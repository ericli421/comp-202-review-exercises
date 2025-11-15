def shift_up(input_list):

    """
    Write a function that takes as input a list. It "shifts up" the list
    by taking the last element of the list and bring it to the front

    You can assume the list to be non-empty

    Arguments:
        input_list: list of elements
    
    Returns: 
        None

    >>> input_list = [12, 43, 0, 4.12, "apple"]
    >>> shift_up(input_list)
    >>> print(input_list)
    ['apple', 12, 43, 0, 4.12]
    >>> shift_up(input_list)
    >>> print(input_list)
    [4.12, 'apple', 12, 43, 0]
    >>> shift_up(input_list)
    >>> print(input_list)
    [0, 4.12, 'apple', 12, 43]
    """

    last_element = input_list.pop(-1)
    input_list.insert(0, last_element)
    
    # Alternatively, here's how you can write it without list methods
    ############################################
    # last_element = input_list[-1]
    # for i in range(len(input_list)-1, 0 ,-1):
    #     input_list[i] = input_list[i-1]
    # input_list[0] = last_element
    ############################################

    # And here's a one line way of writing it that I didn't think about
    ############################################
    # return [my_list[-1]]+ my_list[:-1]
    ############################################