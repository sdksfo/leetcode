
# Explanation:

# For every step, u could have come there from either climbing 1 step or climbing 2 steps
# If we find the minimum path to get to the given step, we can create the DP table
# The final answer is the minimum for (DP[-1], DP[-2])

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0,0] + [0] * len(cost)
        for i in xrange(len(cost)):
        	dp[i+2] = min(dp[i]+cost[i], dp[i+1]+cost[i])
        return min(dp[-1], dp[-2])

print Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
