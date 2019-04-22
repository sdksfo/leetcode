
"""
If monotonic increasing, we hope the peak will lie on the right, else assume its on the left
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums)-1

        while i < j:
        	mid = i + (j-i)/2
        	if (nums[mid] < nums[(mid+1)%len(nums)]):
        		i = mid + 1
        	else:
        		j = mid

        return i

print Solution().findPeakElement([1,2])
