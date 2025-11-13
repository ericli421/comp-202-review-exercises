# comp-202-review-exercises

Collection of review exercises for COMP 202 midterm review organized by McGill CSUS.

## Question: Vowels counter (Strings, Loops)

Difficulty: 2/5

For this question, write a function `count_vowels` that will take as input a string `expression` and return an integer that represents the number of vowels inside of it.

## Question: Longest string of repeating characters (Strings, Loops)

Difficulty: 3/5

For this question, write a function `longest_repeating` that will take as input a string `expression` and return an integer that represents the length of the longest sequence of repeating characters.

## Question: Shift up (1D Lists)

Difficulty: 1/5

Write a function `shift_up` that takes input a list. The function will then take the last element of the list, and move it to the start of the list. Here's an example usage

```python
>>> a = [1,2,3,4,5]
>>> shift_up(a)
>>> print(a)
[5,1,2,3,4]
```

You can assume the list has at least one element in it

## Question: Maximum integer in a list (1D lists, Loops)

Difficulty: 1/5

You've probably used the `max()` function while coding in python at some point. For the purposes of this exercise, you are not allowed to use it.

Write a function `my_max()` that takes as input a list of numbers (either integers or floats), and return the one that has the highest value. In other words, write the code that would make the built-in `max()` function work

## Question: Watered down sudoku (2D Lists and loops)

Difficulty: 5/5

Sudoku is a game where you try to fill a 9x9 board with numbers 1 to 9. The rules are that the numbers cannot reappear twice on each row, each column, or each 3x3 box. For the purposes of this exercise, we will ignore the 3x3 box rule.

A sudoku board can pretty easily be represented as a 2d list of integers in a matrix format. We will use 0 if a cell is empty. Otherwise it has the digit 1-9 in it.

For this exercise, you will write three functions.

- Write a function `valid_row(n, board)` that checks whether or not the row given by `n` in `board` is valid. That is, there are no repeating integers.
- Write a function `valid_col(n, board)` that checks whether or not the column given by `n` in `board` is valid.
- Write a function `valid_board(board)` that checks whether or not the board given by `board` is valid in terms of its rows and columns.

You may assume the value `board` is a 2d list of size 9x9, and the value `n` is an integer between 0 and 8 (both inclusive)

> Challenge: Implement the full sudoku board validator by also checking if a given box is valid.

## Question: Find substrings (Strings)

Difficulty: 2/5

Write a function called `count_substrings()` that will take as input two strings: an `input_string` that contains text, and a `substring`. The function will return an integer that represents the number of times `substring` appears in `input_string`. For example

```python
>>> input_string = "Hello, beautiful weather today. Today, I have to host a review for COMP 202"
>>> substring = "Today"
>>> print(count_substrings(input_string, substring))
2
```

> The function is case insensitive. For example `'Hello' == 'HELLO' == 'hello' == 'HeLlO'`

<!-- ## Question: Add spaces (Strings, loops)

Difficulty: 4/5

Write a function called `add_space`. The function will take an input string, and return a string containing the same characters as the input string. However, when it detects an upper case character between two lower case characters it will add a space before the upper case characters. Use a for loop to traverse the string

```python
>>> add_space('HelloHowAreYouDoing')
Hello How Are You Doing
>>> add_space('IAbsolutelyLOVEIceCream')
IAbsolutelyLOVEIce Cream
>>> add_space('microwave')
microwave
``` -->

## Question: List to String (Strings, 2d lists)

Difficulty: 2/5

Write a function called `list2string`. This function takes in a 2d square list and converts it into a string, going top to bottom, left to right, and returns the final string.

```python
>>> list2string([['H','e','l','l'],['o','o',' ','B','y'],['e']])
Helloo Bye
>>> list2string([['H','a','H','a']])
HaHa
```

## Question: Alternating characters concatenation (Strings, loops)

Difficulty: 3/5

Write the following function

```python
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
```
