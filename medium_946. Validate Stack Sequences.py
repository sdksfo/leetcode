

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        j, stack = 0, []

        for i in xrange(len(pushed)):
        	stack.append(pushed[i])
        	while stack and stack[-1] == popped[j]:
        		stack.pop()
        		j += 1

        return not stack

print Solution().validateStackSequences([1,3,2], [1,2,3])
