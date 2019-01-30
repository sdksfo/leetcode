
# Explanation:

# From the last row and from the last column there is exactly one way to reach the destination. So we fill the DP table as 1 for those.
# Iterate from penultimate row and penultimate column all the way to (0, 0), where dp[i][j] = dp[i+1][j] + dp[i][j+1]
# ie unique paths going down + unique paths going in right


class Solution(object):
    def uniquePaths(self, cols, rows):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1]*(cols)]*(rows)

        for i in xrange(rows-2, -1, -1):
        	for j in xrange(cols-2, -1, -1):
        		dp[i][j] = dp[i+1][j] + dp[i][j+1]

        return dp[0][0]

print Solution().uniquePaths(3, 2)
