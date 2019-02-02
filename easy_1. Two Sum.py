
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in xrange(len(nums)):
        	for j in xrange(i+1, len(nums)):
        		if nums[i] + nums[j] == target:
        			return [i, j]

print Solution().twoSum([3,2,4], 6)