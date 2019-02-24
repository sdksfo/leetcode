

class Solution(object):
    def isValid(self, board, x, y, n):
        return not any([(x, y) != (r, c) and board[r][c] == 'Q' and (abs(x-r) == abs(y-c) or c == y) for r in range(n) for c in range(n)])

    def placeQueens(self, board, row, n):
        if row == n:
            self.result.append([''.join(row) for row in board])
            return
        for col in xrange(n):
            if self.isValid(board, row, col, n):
                board[row][col] = 'Q'
                self.placeQueens(board, row+1, n)
                board[row][col] = '.'

    def solveNQueens(self, n):
        self.result = []
        board = [["."] * n for i in xrange(n)]
        self.placeQueens(board, 0, n)
        return self.result

print Solution().solveNQueens(4)
