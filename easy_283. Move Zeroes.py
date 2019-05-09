

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_idx = 0

        for i in xrange(len(nums)):
        	if nums[i] != 0:
        		nums[i], nums[zero_idx] = 0, nums[i]
        		zero_idx += 1

        return nums

print Solution().moveZeroes([0,0,0,0,0,])
