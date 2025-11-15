def add_space(input_string: str):
    """
    Write a function that takes an input string. The function 
    will return a copy of the string, but with a space added 
    before every capital letter. 
    
    You can assume the string to be non-empty and 
    only containing letters.

    Args:
        input_string: string

    Returns:
        str: input_string with spaces added before all capital letters

    >>> add_space("hiIAmPleasedToMeetYou")
    'hi I Am Pleased To Meet You'
    >>> add_space("I")
    ' I'
    >>> add_space("unicorn")
    'unicorn'
    """
    
    output_string = ""

    for c in input_string:

        if c.upper() == c:
            output_string += " "
            
        output_string += c

    return output_string