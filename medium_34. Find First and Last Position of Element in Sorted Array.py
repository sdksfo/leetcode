
"""
Two binary search, if number is found and

a) idx is non-i and left number is current number: search left, else return current index
b) idx is non-j and right number is current number: search right, else return current index
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def search(i, j, l_index=False):
        	if i > j:
        		return -1
        	m = (i + j)/2
        	if nums[m] == target and l_index:
        		if m > i and nums[m-1] == target:
        			return search(i, m-1, l_index)
        		return m
        	elif nums[m] == target:
        		if m < j and nums[m+1] == target:
        			return search(m+1, j, l_index)
        		return m
        	elif nums[m] > target:
        		return search(i, m-1, l_index)
        	else:
        		return search(m+1, j, l_index)

        return [search(0, len(nums)-1, True), search(0, len(nums)-1, False)]

print Solution().searchRange([5,7,7,8,8,8,8,8,8,10], 7)
