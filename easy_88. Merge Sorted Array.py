"""
Requirement:

Merge two sorted array into one

Approach:

Iterate backwards from the longest array and keep moving the biggest elements using merge sort logic,

Complexity:

Time: O(n) Space: O(1)
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        num_len = len(nums1) - 1

        while m and n:
        	if nums1[m-1] < nums2[n-1]:
        		nums1[num_len] = nums2[n-1]
        		n -= 1
        	else:
        		nums1[num_len] = nums1[m-1]
        		m -= 1
        	num_len -= 1

        if n:
            nums1[:num_len+1] = nums2[:n]
