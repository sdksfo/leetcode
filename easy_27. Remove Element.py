"""
Requirement:

Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Algorithm:

a) Iterate through the array
b) Set the write_idx as 0
c) If the number other than key is found, write the number to the write_idx and increase write_idx
d) If key is found, do not do anything
e) Return write_idx, which is the length of valid elements
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        write_idx = 0

        for num in nums:
        	if num != val:
        		nums[write_idx] = num
        		write_idx += 1

        return write_idx

print Solution().removeElement([3], 3)
