


class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []

        for i in xrange(len(S)):
        	if S[i] == ')':
        		total = 0
        		element = stack.pop()
        		while element != '(':
        			total += element
        			element = stack.pop()
        		stack.append(2*total if total else 1)
        	else:
        		stack.append(S[i])

        return sum(stack)

print Solution().scoreOfParentheses("(()((())))")
