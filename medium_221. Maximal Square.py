
import itertools

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        rows, cols = len(matrix), len(matrix[0]) if matrix else 0

        dp = [[int(matrix[j][i]) for i in range(cols)] for j in range(rows)]

        for r, c in itertools.product(range(1, rows), range(1, cols)):
            if dp[r][c]:
                dp[r][c] = min(dp[r-1][c], dp[r-1][c-1], dp[r][c-1]) + 1

        return max(max(r or [0]) for r in dp or [0]) ** 2

print Solution().maximalSquare([['0']])
