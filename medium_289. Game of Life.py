
import itertools

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows, cols  = len(board), len(board[0]) if board else 0

        output = [[0 for _ in xrange(cols)] for _ in xrange(rows)]

        for row, col in itertools.product(range(rows), range(cols)):
            live = dead = 0
            for r, c in (row+1, col), (row-1, col), (row, col-1), (row, col+1), (row-1, col-1), (row-1, col+1), (row+1, col-1), (row+1, col+1):
                if r not in (-1, rows) and c not in (-1, cols):
                    if board[r][c] == 1:
                        live += 1
                    else:
                        dead += 1
            output[row][col] = 1 if (board[row][col] == 1 and live in (2, 3)) or (board[row][col] == 0 and live == 3) else 0

        for row, col in itertools.product(range(rows), range(cols)):
            board[row][col] = output[row][col]

print Solution().gameOfLife([
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
])
