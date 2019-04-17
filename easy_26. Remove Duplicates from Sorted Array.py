"""
Requirement:

Given a sorted array with duplicates, return length of the new array with unique elements

Algorithm:

a) Iterate through the array and mark the first number as unique.
b) If num is not same as prev num, then swap it with the unique idx.
c) If num is same as prev num, then do not swap with unique idx.

Complexity:

Time - O(n), Space - O(1)
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique = 0

        for i in xrange(1, len(nums)):
            if nums[i] != nums[i-1]:
                unique += 1
                nums[unique] = nums[i]
        return unique + 1

print Solution().removeDuplicates([1])
