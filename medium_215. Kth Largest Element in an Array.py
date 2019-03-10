
import random

class Solution(object):

    def partitionArray(self, array, start, end):
        pivot_idx = start
        for i in xrange(start+1, len(array)):
            if array[i] < array[pivot_idx]:
                array.insert(start, array.pop(i))
                pivot_idx += 1
        return array, pivot_idx

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        smallest = len(nums)-k
        array, pivot_idx = self.partitionArray(nums, 0, len(nums)-1)

        while pivot_idx != smallest:
            if pivot_idx < smallest:
                array, pivot_idx = self.partitionArray(nums, pivot_idx+1, len(nums)-1)
            else:
                array, pivot_idx = self.partitionArray(nums, 0, pivot_idx-1)
        return array[pivot_idx]

print Solution().findKthLargest([3,3,3,3,3,3,3,3,3], 8)

