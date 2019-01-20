
# Explanation:

# For any number, either the number can be part of the array sequence or not choose to be part of int

# dp[n] = max(dp[n-1]+n, n)

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = maxi = nums[0]
        for num in nums[1:]:
        	prev = max(prev+num, num)
        	maxi = max(maxi, prev)
        return maxi

print Solution().maxSubArray([-1])