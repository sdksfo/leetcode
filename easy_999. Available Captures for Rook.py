"""
Requirement:

Capture the pawns that a rook can capture.

Approach:

Determine which position the rook lies and then do a DFS on all four directions

Complexity:

Time: O(1) Space: O(1)
"""

# Using DFS

class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        self.count = 0

        def dfs(row, col, row_inc, col_inc):
            if row in (-1, 8) or col in (-1, 8):
                return
            if board[row][col] == 'p':
                self.count += 1
                return
            if board[row][col] in ('.', 'R'):
                dfs(row+row_inc, col+col_inc, row_inc, col_inc)

        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    dfs(i, j,  0, -1), dfs(i, j,  0,  1), dfs(i, j, -1,  0), dfs(i, j,  1,  0)
                    break

        return self.count

# Using plain array logic

class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        self.count = 0

        def remove_dot(s):
            return s != '.'

        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    prc = filter(remove_dot, board[i][:j])
                    poc = filter(remove_dot, board[i][j+1:])
                    prr = filter(remove_dot, [board[t][j] for t in range(i)])
                    por = filter(remove_dot, [board[t][j] for t in range(i+1,8)])

        return (prc and prc[-1] == 'p') + (poc and poc[0] == 'p') + (prr and prr[-1] == 'p') + (por and por[0] == 'p')
