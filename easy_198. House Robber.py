
# Explanation:

# robbery at house(n) = max(house(n-2)+n, house(n-3)+n)

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp, maxi = [0] * (len(nums)+3), 0
        for i in xrange(len(nums)):
        	dp[i+3] = max(dp[i]+nums[i], dp[i+1]+nums[i])
        	maxi = max(dp[i+3], maxi)
        return maxi

print Solution().rob([2,7,9,6,1])