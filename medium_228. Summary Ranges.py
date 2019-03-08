

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        stack, output = [str(nums[0])] if nums else [], []

        for i in xrange(1, len(nums)):
        	if nums[i-1] + 1 != nums[i]:
        		output.append((stack[0] + '->' + stack[-1]) if len(stack) > 1 else '->'.join(stack))
        		stack = []
        	stack.append(str(nums[i]))

        if stack:
        	output.append((stack[0] + '->' + stack[-1]) if len(stack) > 1 else '->'.join(stack))

        return output

print Solution().summaryRanges([])
