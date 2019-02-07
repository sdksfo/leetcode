"""
Traverse the grid for every 1 that is encountered and do a DFS traversal to see whats the maximum area that
can be covered. When a 1 is already seen mark it as 0
"""

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols, area = len(grid), len(grid[0]) if grid else 0, 0

        def dfs(row, col, ctr=0):
        	if row not in (-1, rows) and col not in (-1, cols) and grid[row][col]:
        		grid[row][col] = 0
        		ctr = 1 + dfs(row-1, col) + dfs(row+1, col) + dfs(row, col-1) + dfs(row, col+1)
        	return ctr

        for row in xrange(rows):
        	for col in xrange(cols):
        		if grid[row][col]:
        			area = max(dfs(row, col), area)
        return area

print Solution().maxAreaOfIsland([[0]])
