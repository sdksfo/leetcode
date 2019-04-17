"""
Requirement:

Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Approach:

Sort and add the alternative elements

Complexity:

Time: O(nlogn) + O(n) Space: O(1)
"""


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return sum(nums[i] for i in xrange(0, len(nums), 2))
