
"""
This problem is the same as number of connected components. For
each '1' that is not visited yet traverse to all its connected nodes
and mark them as seen.
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows, cols, islands = len(grid), len(grid[0]) if grid else 0, 0

        def dfs(row, col):
            if row not in (-1, rows) and col not in (-1, cols) and grid[row][col] == '1':
                grid[row][col] = 0
                dfs(row+1, col), dfs(row-1, col), dfs(row, col+1), dfs(row, col-1)

        for row in xrange(rows):
            for col in xrange(cols):
                if grid[row][col] == '1':
                    islands += 1
                    dfs(row, col)

        return islands

print Solution().numIslands(
    [['1','1',0,0,0],
    ['1','1',0,0,0],
    [0,0,'1',0,0],
    [0,0,0,'1','1']])

