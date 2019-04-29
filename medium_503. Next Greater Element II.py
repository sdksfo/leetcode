
"""
Same as next greater element. But iterate again if the first step results in a non empty stack
"""

class Solution(object):

    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack, output = [], [-1 for _ in nums]

        def getNextGreater(i):
            while stack and nums[stack[-1]] < nums[i]:
                output[stack.pop()] = nums[i]
            stack.append(i)

        for i in xrange(len(nums)):
        	getNextGreater(i)

        for i in xrange(stack[-1] if stack else 0):
            getNextGreater(i)

        return output

print Solution().nextGreaterElements([])
