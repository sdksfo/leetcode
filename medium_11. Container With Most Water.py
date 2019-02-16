
"""
Problem:

https://leetcode.com/problems/container-with-most-water/

Solution:

Using two pointer, enclosed area is directly proportional to the size of shorter line. We use the two pointer technique and adjust the pointer
depending on which side is shorter.
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area, i, j = 0, 0, len(height)-1

        while i < j:
        	if height[i] < height[j]:
        		max_area = max(max_area, height[i]*(j-i))
        		i += 1
        	else:
        		max_area = max(max_area, height[j]*(j-i))
        		j -= 1
        return max_area

print Solution().maxArea([1,8,6,2,5,4,8,3,7])
