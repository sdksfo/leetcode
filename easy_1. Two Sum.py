

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}

        for i, d in enumerate(nums):
        	if target - d in hashmap:
        		return [i, hashmap[target-d]]
        	hashmap[d] = i

