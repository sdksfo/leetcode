
# Explanation

# min cost for i,j = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]

import sys

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [[sys.maxint for i in xrange(len(grid[0])+1)]] + [[sys.maxint]+grid[i] for i in xrange(len(grid))]
        dp[0][1] = 0
        for i in xrange(len(grid)):
        	for j in xrange(len(grid[0])):
        		dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1]) + grid[i][j]
        return dp[-1][-1]

print Solution().minPathSum([[1,2,5],[3,2,1]])
