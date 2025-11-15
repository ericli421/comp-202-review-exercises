def alternate(s1,s2):
    """
    Takes as input two strings. It returns a string that 
    is alternating characters of the two strings
    Arguments:
        s1 (str): first string
        s2 (str): second string
    Returns:
        string: result that alternates between both strings
    >>> alternate("ace","bdf")
    'abcdef'
    >>> alternate("I love", "Ice Cream")
    'II cleo vCeream'
    >>> alternate("Hello World!", "")
    'Hello World!'
    """

    i=0
    output_str = ""
    while i < max(len(s1),len(s2)):
        if i < len(s1):
            output_str += s1[i]

        if i < len(s2):
            output_str += s2[i]
        i+=1
    
    return output_str
