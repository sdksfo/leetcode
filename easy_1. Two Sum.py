
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(nums) - 1

        while i < j:
        	if nums[i] + nums[j] == target:
        		return [i, j]
        	elif nums[i] + nums[j] > target:
        		j -= 1
        	else:
        		i += 1