
"""
For any given number, traverse back and check what is the highest number there is that is just lower than current number that could maximise it.
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp, maxseq = [1] * len(nums), 0

        for i in xrange(len(nums)):
        	curr_seq = 1
        	for j in xrange(i):
        		if nums[i] > nums[j] and dp[j] >= curr_seq:
        			curr_seq = dp[j]+1
        	dp[i] = curr_seq
        	maxseq = max(curr_seq, maxseq)

        return maxseq

print Solution().lengthOfLIS([0,5,2,3,4,0,9])
