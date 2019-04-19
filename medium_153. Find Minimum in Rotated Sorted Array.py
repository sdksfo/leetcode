"""
Even though the array is rotated, if we split the array in the mid, atleast one of the sides is monotonically increasing.
We will use that property to drive the search.

Complexity: O(logn)
"""

class Solution(object):
    def findMin(self, nums):

    	def search(i, j):
    		mid = (i + j) / 2

    		if (nums[(mid+1)%len(nums)] >= nums[mid] <= nums[mid-1]):
    			return nums[mid]
    		elif nums[mid] >= nums[i]:
    			return search(i, mid-1) if nums[i] < nums[j] else search(mid+1, j)
    		else:
    			return search(i, mid-1) if nums[i] > nums[j] else search(mid+1, j)

    	return search(0, len(nums)-1)
