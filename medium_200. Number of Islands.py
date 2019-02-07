
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
        rows, cols, seen, islands = len(grid), len(grid[0]) if grid else 0, set(), 0

        def dfs(row, col, seen):
            if row not in (-1, rows) and col not in (-1, cols) and (row, col) not in seen and grid[row][col] == '1':
                seen.add((row, col))
                dfs(row+1, col, seen), dfs(row-1, col, seen), dfs(row, col+1, seen), dfs(row, col-1, seen)
            return seen

        for row in xrange(rows):
            for col in xrange(cols):
                if grid[row][col] == '1' and (row, col) not in seen:
                    islands += 1
                    seen = dfs(row, col, seen)

        return islands

print Solution().numIslands(
    [['1','1',0,0,0],
    ['1','1',0,0,0],
    [0,0,'1',0,0],
    [0,0,0,'1','1']])

