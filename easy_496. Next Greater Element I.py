
"""
a) Iterate from left to right on nums2
b) For each number in the nums2, check against the stack and see if there is a smaller number seen
c) If so, pop from stack and add it to a hashmap
d) If not, add the number to the stack
"""

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack, hashmap = [], {}

        for num in nums2:
        	while stack and num > stack[-1]:
        		hashmap[stack.pop()] = num
        	stack.append(num)

        while stack:
        	hashmap[stack.pop()] = -1

        return [hashmap[num] for num in nums1]

print Solution().nextGreaterElement([2,4], [1,2,3,4])
