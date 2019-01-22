# Explanation:

# This is the DNF problem: https://en.wikipedia.org/wiki/Dutch_national_flag_problem

# For sorting an array of 3 different numbers, if we push the `low` numbers to the left and
# `high` numbers to the right, the `mid` numbers would automatically be in order.

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_ptr, two_ptr, i = 0, len(nums) - 1, 0

        while i <= two_ptr:
        	if nums[i] == 0:
        		nums[i], nums[zero_ptr] = nums[zero_ptr], nums[i]
        		zero_ptr += 1
        		i += 1
        	elif nums[i] == 2:
        		nums[i], nums[two_ptr] = nums[two_ptr], nums[i]
        		two_ptr -= 1
        	else:
        		i += 1
        return nums

print Solution().sortColors([0,2,1])
