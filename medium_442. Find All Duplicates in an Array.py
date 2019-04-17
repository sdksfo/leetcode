"""
Requirement:

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Approach:

Use the negation technique ie when a number is found, mark its index in the array as negative.

Complexity:

Time: O(n) Space: O(1)
"""

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []

        for i, d in enumerate(nums):
        	if nums[abs(d)-1] < 0:
        		output.append(abs(d))
        	else:
        		nums[abs(d)-1] = 0 - nums[abs(d)-1]

        return output

print Solution().findDuplicates([4,3,2,7,8,2,3,1])
