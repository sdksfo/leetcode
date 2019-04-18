"""
Approach:

a) Use shorter array and binary search on the longer array

Time: O(logn) Space: O(1)
"""

class Solution(object):
    def find_num(self, n, target, i, j):
        if i > j:
            return -1
        mid = (i+j)/2
        if n[mid] == target:
            return mid
        elif n[mid] > target:
            return self.find_num(n, target, i, mid-1)
        else:
            return self.find_num(n, target, mid+1, j)

    def search(self, n1, n2):
        return [i for i in set(n1) if self.find_num(n2, i, 0, len(n2)-1) != -1]

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1, nums2 = sorted(nums1), sorted(nums2)

        return self.search(nums1, nums2) if len(nums1) < len(nums2) else self.search(nums2, nums1)
