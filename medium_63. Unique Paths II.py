
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
        rows, cols = len(grid), len(grid[0])
        dp = [[int(not grid[row][col]) for col in xrange(cols)] for row in xrange(rows)]
        for i in xrange(cols-2, -1, -1):
        	dp[-1][i] = 0 if grid[-1][i] or not dp[-1][i+1] else dp[-1][i]
        for i in xrange(rows-2, -1, -1):
        	dp[i][-1] = 0 if grid[i][-1] or not dp[i+1][-1] else dp[i][-1]
        for row in xrange(rows-2, -1, -1):
        	for col in xrange(cols-2, -1, -1):
        		dp[row][col] = 0 if grid[row][col] else dp[row+1][col] + dp[row][col+1]
        return dp[0][0]

print Solution().uniquePathsWithObstacles([[0,0], [0,0]])
