

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for num in nums]

        for i in xrange(len(nums)-2, -1, -1):
        	mini = len(nums)
        	for t in xrange(i+1, min(i+nums[i]+1, len(nums))):
        		mini = min(dp[t], mini)
        	dp[i] = 1 + mini

        return dp[0]

print Solution().jump([2])
