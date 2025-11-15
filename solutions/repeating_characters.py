def longest_repeating(expression):
    """
    Write a function that takes in an input string. The function 
    will then go through every character and count the longest
    sequence of repeating characters. It will then return 
    an integer that is the longest count 
    
    Arguments:
        expression: str
    
    Returns:
        int: longest sequence of repeating characters

    >>> longest_repeating("Hello World!")
    2
    >>> longest_repeating("aAaaabAAA")
    5
    >>> longest_repeating("I love ice cream")
    1
    """

    count = 0
    max_len = 0

    if len(expression) != 0:

        current_char = expression[0].lower()

        for i in range(len(expression)):
            if current_char == expression[i].lower():
                count += 1
            else:
                if count > max_len:
                    max_len = count
                count = 1
                current_char = expression[i].lower()
    
    return max_len