
""" Iterate through the matrix, when a 1 is encountered, do a DFS of the corresponding row as long as its row is not visited """

import itertools

class Solution(object):
    def findCircleNum(self, grid):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        rows, cols, groups = len(grid), len(grid[0]) if grid else [], 0

        def dfs(row):
            for col in xrange(cols):
                if grid[row][col]:
                    grid[row][col] = 0
                    dfs(col)

        for row in xrange(rows):
            if grid[row][row]:
                groups += 1
                dfs(row)

        return groups

print Solution().findCircleNum([[1]])
