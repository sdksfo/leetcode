"""
Tip: A plain vanilla binary search will return the index if number is found, else the index will point at where the number can be inserted.

O(logn)
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i, j = 0, len(nums) - 1

        while i <= j:

        	mid = (i + j)/2

        	if (nums[mid] == target):
        		return mid
        	elif nums[mid] > target:
        		j = mid-1
        	else:
        		i = mid+1

        return i


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0]: return 0

        if target > nums[-1]: return len(nums)

        i, j = 0, len(nums) - 1

        while i <= j:

        	mid = (i + j)/2

        	if (nums[mid] == target) or (nums[mid-1] < target < nums[mid]):
        		return mid
        	elif nums[mid] < target < nums[mid+1]:
        		return mid+1
        	elif nums[mid] > target:
        		j = mid-1
        	else:
        		i = mid+1

print Solution().searchInsert([1,3,5,6], 3)
