
"""
Go through each number from 1..10 and recursively compute if the total is reachable
"""

class Solution(object):
    def combinationSum3(self, size, total, nums=range(1, 10)):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if size == 1:
        	return [[total]] if total in nums else []
        output = []
        for i in xrange(len(nums)):
        	if nums[i] < total:
        		solutions = self.combinationSum3(size-1, total - nums[i], nums[i+1:])
        		output.extend([[nums[i]] + j for j in solutions]) if solutions else None
        return output

print Solution().combinationSum3(3,9)
