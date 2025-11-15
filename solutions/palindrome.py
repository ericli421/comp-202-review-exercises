def is_palindrome(input_string):
    """
    Checks whether the given string is a palindrome
    Returns a boolean based on whether it is

    Arguments:
        input_string: string
    
    Returns:
        bool: True if input_string is a palindrome

    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("hello")
    False
    >>> is_palindrome("nom mon")
    True
    """
    
    ### APPROACH 1
    # return input_string == input_string[::-1]

    ### APPROACH 2
    for i in range(len(input_string)):
        if input_string[i] != input_string[len(input_string) - i - 1]:
            return False
        
    return True


import doctest
doctest.testmod(verbose=True)