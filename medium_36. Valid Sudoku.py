"""
Requirement:
Validate if the filled cells in the 9x9 sudoku board are valid. Valid is when
a) Each row only has numbers from 1-9 without repetition
b) Each column only has numbers from 1-9 without repetition
c) Each of the 9 3x3 boxes have rules like above

Algorithm:
a) Helper function is_valid() - Accepts an array of 9 numbers and checks if valid according to rules above.
b) For row validity
For each row, call the is_valid().
c) For col validity
For each col, create the array of 9 numbers and call is_valid()
d) For 3x3 row validity,
Slide through rows in steps of 3:
    For each row slide the columns in steps of 3
    for first row, it becomes:
        (0,0)->(2,2) (0,3)->(2,5) (0,6)->(2,8)

Complexity:

Time - O(rowxcol), Space - O(row)
"""

import itertools

class Solution(object):
    def is_valid(self, cells):
        visited = set()
        for num in cells:
            if num != '.' and num in visited: return False
            visited.add(num)
        return True

    def valid_rows(self, board):
        for row in board:
            if not self.is_valid(row): return False
        return True

    def valid_cols(self, board):
        for col in range(9):
            array = [board[row][col] for row in range(9)]
            if not self.is_valid(array): return False
        return True

    def valid_boxes(self, board):
        for row in xrange(0, 9, 3):
            for col in range(0, 9, 3):
                array = [board[r][c] for r, c in itertools.product(range(row, row+3), range(col, col+3))]
                if not self.is_valid(array): return False
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.valid_rows(board) and self.valid_cols(board) and self.valid_boxes(board)

print Solution().isValidSudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
])
