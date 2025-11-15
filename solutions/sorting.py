def my_sort(input_list):
    """
    Write a function that implements the bubble sorting algorithm on
    a list of numbers

    Arguments:
        input_list: list of numbers

    Returns:
        None

    >>> a = [6,2,4,5,7,8]
    >>> my_sort(a)
    >>> print(a)
    [2, 4, 5, 6, 7, 8]
    >>> b =[173,-120,439,0]
    >>> my_sort(b)
    >>> print(b)
    [-120, 0, 173, 439]
    >>> c = [1.32,5.43,-12.32,-1.1]
    >>> my_sort(c)
    >>> print(c)
    [-12.32, -1.1, 1.32, 5.43]
    """

    for i in range(len(input_list)-1):

        for j in range(0, len(input_list)-1):

            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]

import doctest; doctest.testmod(verbose=True)