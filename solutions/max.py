def my_max(input_list):

    """
    Write a function that takes as input a list of integers and returns the integer 
    with the highest value. You can assume the list to be non-empty
    
    Constraints: you are not allowed to use the max() function

    Arguments:
        input_list: list of integers

    Returns:
        int: integer in the list with the highest value

    >>> my_max([1,2,3,5])
    5
    >>> my_max([-1000000,12])
    12
    >>> my_max([123123,243231243,21349234,9788645,18231230953409])
    18231230953409
    """

    highest = input_list[0]

    for num in input_list:
        if num > highest:
            highest = num
    
    return highest
