"""
Requirement:

Check degree of an array

Approach:

a) Use a list to store all indices for every number in nums
b) Where length of list is equal to the degree of array, compute how far these elements are in the array and get the number with the smallest distance

Complexity:

Time: O(n) Space: O(n)
"""

import collections

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ctrs, max_len, min_len = collections.defaultdict(list), 0, len(nums)

        for i, d in enumerate(nums):
        	ctrs[d].append(i)
        	max_len = max(max_len, len(ctrs[d]))

        for num, indices in ctrs.items():
            if len(indices) == max_len:
        		min_len = min(min_len, indices[-1] - indices[0] + 1)

        return min_len
