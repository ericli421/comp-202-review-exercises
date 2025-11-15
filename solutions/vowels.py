def count_vowels(expression):
    """
    Write a function that takes a string as input. The
    function will return an integer representing the number
    of vowels in the input string

    Args:
        expression (str): Input string

    Returns:
        int: Num of vowels in expression

    >>> count_vowels("Hello World!")
    3
    >>> count_vowels("Twelve Elephants crossing the street")
    10
    >>> count_vowels("Come to Trottier 3090 between 11-5 for more tutoring help")
    16
    """


    vowels = 'aeiouy'
    count = 0

    for c in expression.lower():
        if c in vowels:
            count += 1

    return count