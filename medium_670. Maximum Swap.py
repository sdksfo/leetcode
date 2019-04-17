"""
Requirement:

Maximise the number by performing at most 1 swap

Approach:

a) For each digit in the number, check if there is a bigger number on the right that we could swap with and maximise the output.
b) If such a swap is possible, return the maximum number computed.

Only thing to consider during the swap is that we cannot swap with the first bigger number when traversing from left to right,
consider this e.g

291091

Swapping the '9' at index 1 with '2' results in 921091 which is smaller than when swapping the '2' with '9' at index 4.

The reason is that swapping the '2' with bigger number is basically making the MSB bigger, but at the same time the smaller number should
be placed at the LSB. So ideally moving '2' to index 4 will maximise our number than placing at index 1.

Complexity:

Time: O(n*n) Space: O(1)
"""

class Solution(object):
    def maximumSwap(self, nums):
        """
        :type num: int
        :rtype: int
        """
        max_num, nums = nums, str(nums)

        for i in xrange(len(nums)):
        	for j in xrange(i+1, len(nums)):
        		if nums[j] > nums[i]:
        			max_num = max(max_num, int(nums[:i] + nums[j]+nums[i+1:j] + nums[i] + nums[j+1:]))
        	if max_num > int(nums): return max_num

        return int(nums)
