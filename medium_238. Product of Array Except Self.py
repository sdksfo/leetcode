"""
a) Iterate twice, once forward and next backwards
b) During forward iteration, store the products of all numbers to the left of current number in the o/p array
c) During backward iteration, compute the product of all numbers to the right of current number but also update with the index in the o/p array.

Time: O(n) Space: O(1)
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output, before, after = [], 1, 1

        for num in nums:
        	output.append(before)
        	before *= num

        for i in xrange(len(nums)-1, -1, -1):
        	output[i] *= after
        	after *= nums[i]

        return output
