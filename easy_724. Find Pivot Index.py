"""
Requirement:

Given an array of integers nums, write a method that returns the "pivot" index of this array.

Approach:

Get a running sum and total sum and find if the curr * 2 == total - num

Complexity:

Time: O(n) Space: O(1)
"""

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total, curr = sum(nums), 0

        for i, num in enumerate(nums):
        	if curr << 1 == (total - num):
        		return i
        	curr += num
        return -1
