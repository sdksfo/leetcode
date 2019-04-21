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
        i, j = 0, len(nums)

        while i < j:
            mid = (i + j)/2
            if (nums[mid] == target):
                return mid
            elif nums[mid] > target:
                j = mid
            else:
                i = mid+1

        return i

print Solution().searchInsert([1,3,5,6], 3)
