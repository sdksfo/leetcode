"""
The search criteria is from 1 through len(nums)-1.

We choose a mid number and check if the count of elements <= mid is greater than the element itself, in which case
we direct our search in left or right direction
"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 1, len(nums)-1

        while i < j:
        	mid = i + (j - i)/2
        	if sum(1 for t in nums if t<=mid) > mid:
        		j = mid
        	else:
        		i = mid + 1

        return i

print Solution().findDuplicate([2,5,9,6,9,3,8,9,7,1])
