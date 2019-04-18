


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ctr, max_ctr = 0, 0

        for num in nums:
        	if num == 0:
        		max_ctr = max(max_ctr, ctr)
        		ctr = 0
        	else:
        		ctr += 1

        return max(max_ctr, ctr)
