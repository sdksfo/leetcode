
"""
Problem:

https://leetcode.com/problems/search-in-rotated-sorted-array/

Solution:

Try to identify which side is sorted, and then depending on if target is reachable
or not drive the binary search in that direction

Time Complexity:

O(logn)
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def get_item(i, j):
            if i > j:
                return -1
            mid = (i+j)/2
            if nums[mid] == target:
                return mid
            if nums[i] <= nums[mid]:
                return get_item(i, mid-1) if nums[i] <= target < nums[mid] else get_item(mid+1, j)
            if nums[mid] <= nums[j]:
                return get_item(mid+1, j) if nums[mid] < target <= nums[j] else get_item(i, mid-1)
        return get_item(0, len(nums)-1)

print Solution().search([4,5,6,7,0,1,2], 3)
