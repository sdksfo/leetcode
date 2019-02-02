
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, d in enumerate(nums):
        	if target - d in seen:
        		return [seen[target-d], i]
        	seen[d] = i

print Solution().twoSum([3,2,4], 6)
