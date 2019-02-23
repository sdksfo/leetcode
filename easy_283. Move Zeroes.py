
"""
Iterate through the array, if a zero is encountered, mark the position as
the first 0th index. If a number is found, swap it with the 0th index and
increase the 0th index value.
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_index, i = None, 0

        while i < len(nums):
        	if nums[i] == 0 and zero_index is None:
        		zero_index = i
        	if nums[i] != 0 and zero_index is not None:
        		nums[i], nums[zero_index] = nums[zero_index], nums[i]
        		zero_index += 1
        	i += 1

        print nums

print Solution().moveZeroes([0,1])
