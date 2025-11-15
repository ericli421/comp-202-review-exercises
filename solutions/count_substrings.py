def count_substrings(input_string, substring):
    """
    This function takes in as input a string, and a substring to check for.
    It will count the number of time the substring appears in the string,
    ignoring capitalization. It returns that number.

    Make sure you consider overlap. For example, "ABABAB" contains 2 
    instances of the substring "ABAB" 

    You can assume the arguments are non-empty

    Arguments:
        input_string: str 
        substring: str

    Returns:
        int: number of times substring appears in input_string

    >>> count_substrings("HELLO WORLD", "ell")
    1
    >>> count_substrings("i like ice cream", "chocolate")
    0
    >>> count_substrings("ABABAB", "ABAB")
    2
    """

    if len(substring) > len(input_string):
        return 0
    
    count = 0
    end_index = len(input_string) - len(substring) + 1

    for i in range(0, end_index):

        current_segment = input_string[i:i+len(substring)].lower()

        if current_segment == substring.lower():
            count += 1

    return count
