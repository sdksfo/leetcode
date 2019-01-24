
# Explanation

# For any number e.g 12

# We look at all the perfect squares until that number and do a min calculation

# e.g for 12, the squares until 12 are 1, 4, 9

# therefore 12 = min(1+dp[11], 4+dp[8], 9+dp[3]) = 3

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = [i*i for i in xrange(1, n+2)]
        dp = [0 for i in xrange(n+1)]
        for i in xrange(1, n+1):
            mini, j = i, 0
            while squares[j] <= i:
                mini = min(mini, 1 + dp[i-squares[j]])
                j += 1
            dp[i] = mini
        return dp[i]

print Solution().numSquares(8829)