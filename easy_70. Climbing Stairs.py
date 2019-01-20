# Explanation

# You can get to step n from either n-1 or n-2

# no.of ways to step 'n' = no.of ways to n-1 + no.of ways to n-2


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 1] + [0] * n # 0 and 1 here since, we can take 1 step to get to first 1 step and two steps to step 1 is not possible

        for i in xrange(n):
        	dp[i+2] = dp[i] + dp[i+1]

        return dp[-1]

print Solution().climbStairs(4)
