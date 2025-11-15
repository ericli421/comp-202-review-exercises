# If this was an actual project, it would be better to find the size of the board
# and use that instead of hard coding the value 9
# This would make these functions easier to scale for larger boards
# Putting the value 9 here is fine though

def valid_row(row, board):
    """
    Write a function that tests whether a given row on a 
    sudoku board is valid

    Args:
        row (int): row index
        board (2d list of ints): sudoku board

    Returns:
        bool: True if the row is valid by sudoku rules

    >>> board = [[0, 6, 0, 2, 0, 0, 0, 0, 9], 
    ...          [0, 0, 0, 0, 7, 0, 0, 3, 0], 
    ...          [0, 5, 0, 0, 0, 0, 4, 0, 0], 
    ...          [1, 0, 0, 0, 0, 0, 0, 8, 0], 
    ...          [0, 0, 0, 5, 5, 4, 0, 0, 0], 
    ...          [0, 0, 0, 6, 0, 0, 0, 0, 0], 
    ...          [2, 0, 0, 0, 0, 0, 9, 0, 5], 
    ...          [0, 0, 9, 0, 8, 0, 0, 0, 0], 
    ...          [0, 0, 0, 0, 0, 0, 6, 0, 9]]
    >>> valid_row(0, board)
    True
    >>> valid_row(4, board)
    False
    >>> valid_row(8, board)
    True
    """

    already_seen = []

    for i in range(9):

        if board[row][i] != 0 and board[row][i] in already_seen:
            return False
        else:
            already_seen.append(board[row][i])

    return True

def valid_col(col, board):
    """
    Write a function that tests whether a given column on a 
    sudoku board is valid

    Args:
        col (int): col index
        board (2d list of ints): sudoku board

    Returns:
        bool: True if the col is valid by sudoku rules

    >>> board = [[0, 6, 0, 2, 0, 0, 0, 0, 9], 
    ...          [0, 0, 0, 0, 7, 0, 0, 3, 0], 
    ...          [0, 5, 0, 0, 0, 0, 4, 0, 0], 
    ...          [1, 0, 0, 0, 0, 0, 0, 8, 0],
    ...          [0, 0, 0, 5, 5, 4, 0, 0, 0], 
    ...          [0, 0, 0, 6, 0, 0, 0, 0, 0], 
    ...          [2, 0, 0, 0, 0, 0, 9, 0, 5], 
    ...          [0, 0, 9, 0, 8, 0, 0, 0, 0], 
    ...          [0, 0, 0, 0, 0, 0, 6, 0, 9]]
    >>> valid_col(0, board)
    True
    >>> valid_col(4, board)
    True
    >>> valid_col(8, board)
    False
    """

    already_seen = []

    for i in range(9):

        if board[i][col] != 0 and board[i][col] in already_seen:
            return False
        else:
            already_seen.append(board[i][col])
    
    return True


def valid_sudoku(board):
    """
    Write a function that tests whether a given row on a 
    sudoku board is valid

    Args:
        board (2d list of ints): sudoku board

    Returns:
        bool: True if the board is valid by sudoku rules

    >>> board1 = [[0, 6, 0, 2, 0, 0, 0, 0, 9], 
    ...           [0, 0, 0, 0, 7, 0, 0, 3, 0], 
    ...           [0, 5, 0, 0, 0, 0, 4, 0, 0], 
    ...           [1, 0, 0, 0, 0, 0, 0, 8, 0], 
    ...           [0, 0, 0, 5, 5, 4, 0, 0, 0], 
    ...           [0, 0, 0, 6, 0, 0, 0, 0, 0], 
    ...           [2, 0, 0, 0, 0, 0, 9, 0, 5], 
    ...           [0, 0, 9, 0, 8, 0, 0, 0, 0], 
    ...           [0, 0, 0, 0, 0, 0, 6, 0, 9]]
    >>> valid_sudoku(board1)
    False
    >>> board2 = [[0, 6, 0, 2, 0, 0, 0, 0, 0], 
    ...           [0, 0, 0, 0, 7, 0, 0, 3, 0], 
    ...           [0, 5, 0, 0, 0, 0, 4, 0, 0], 
    ...           [1, 0, 0, 0, 0, 0, 0, 8, 0], 
    ...           [0, 0, 0, 5, 0, 4, 0, 0, 0], 
    ...           [0, 0, 0, 6, 0, 0, 0, 0, 0], 
    ...           [2, 0, 0, 0, 0, 0, 9, 0, 5], 
    ...           [0, 0, 9, 0, 8, 0, 0, 0, 0], 
    ...           [0, 0, 0, 0, 0, 0, 6, 0, 0]]
    >>> valid_sudoku(board2)
    True
    >>> board3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
    ...           [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    ...           [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    ...           [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    ...           [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ...           [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    ...           [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    ...           [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    ...           [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    >>> valid_sudoku(board3)
    True
    """
    # I hate docstrings

    for i in range(9):
        
        if valid_row(i,board) == False or valid_col(i,board) == False:
            return False
        
    return True
