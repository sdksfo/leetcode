"""
Approach:

a) Even though the array is rotated, when we cut the array into two halves, atleast one side will be monotonically increasing.
b) We will use this fact to determine if our target is lying on the left monotonic sequence or on the right monotonic sequence.

Time: O(logn) Space: O(1)
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i, j = 0, len(nums) - 1

        while i <= j:
	        mid = (i + j)/2

	        if nums[mid] == target:
	        	return mid
	        elif nums[i] <= nums[mid]: # left side is increasing
	        	if nums[i] <= target < nums[mid]: # and number lies on the left side
	        		j = mid - 1
	        	else:
	        		i = mid + 1
	        elif nums[mid] <= nums[j]: # right side is increasing
	        	if nums[mid] < target <= nums[j]: # and number lies on the right side
	        		i = mid + 1
	        	else:
	        		j = mid - 1

        return - 1
