"""
Requirement:

Given an array of 0s, negative and positive number find the first missing positive

Approach:

a) Iterate through the array
b) For every zero or negative number, mark it as k+1 where k is length of array
c) If number is within 1 thru K, go and mark the position as visited by either negating it or marking as True in boolean table.
d) Iterate again and find the first missing index that is positive or Falsey

Complexity:

Time: O(n), Space: O(1) w/o boolean table else O(n)
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        boolean_table = [False] * (len(nums)+1)

        for i in xrange(len(nums)):
            if nums[i] > 0 and nums[i] < len(boolean_table):
                boolean_table[nums[i]] = True

        for i in xrange(1, len(boolean_table)):
            if not boolean_table[i]:
                return i

        return len(nums) + 1


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in xrange(len(nums)):
            if nums[i] < 1: nums[i] = len(nums) + 1

        for i in xrange(len(nums)):
            if abs(nums[i]) - 1 < len(nums) and nums[abs(nums[i])-1] > 0:
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]

        for i in xrange(len(nums)):
            if nums[i] > 0: return i + 1

        return len(nums) + 1


print Solution().firstMissingPositive([7,8,9,11,12])
