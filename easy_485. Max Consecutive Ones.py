

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count, prev, ctr = 0, 0, 0

        for num in nums:
        	if num == 1:
        		ctr += 1
        	if not num and prev:
        		max_count = max(ctr, max_count)
        		ctr = 0
        	prev = num
        return max(max_count, ctr)

print Solution().findMaxConsecutiveOnes([0])
