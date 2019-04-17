"""
Requirement:

Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.

Approach:

Use DP to add on top of previously built results
Use a 3D array to store the values in each direction

Complexity:

Time: O(m*n) Space: O(m*n*4)
"""

import itertools

class Solution(object):
    def longestLine(self, grid):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0]) if grid else 0

        dp, max_count = [[[0, 0, 0, 0] for _ in range(cols+2)] for _ in range(rows+1)], 0

        for r, c in itertools.product(range(rows), range(cols)):
        	if grid[r][c]:
        		dp[r+1][c+1] = [1 + dp[r][c+1][0], 1 + dp[r+1][c][1], 1 + dp[r][c][2], 1 + dp[r][c+2][3]]
        		max_count = max(max(dp[r+1][c+1]), max_count)

        return max_count
