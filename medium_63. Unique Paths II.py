
# Explanation:

# Same as unique paths problem, but with one additional step:

# We scan the last row and last column of the DP table and reset them to 0 instead of 1, if there is an obstacle
# along the way


class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1: return 0
        for row in xrange(len(grid)):
        	for col in xrange(len(grid[0])):
        		grid[row][col] = 0 if grid[row][col] else ((grid[row-1][col] if row>0 else 0) + (grid[row][col-1] if col > 0 else 0))
        		grid[row][col] = 1 if not row and not col else grid[row][col]
        return grid[-1][-1]
print Solution().uniquePathsWithObstacles([[1]])
