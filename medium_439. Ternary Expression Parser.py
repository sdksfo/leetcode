


class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        stack, i = [], len(expression)-1

        while i > -1:
        	if expression[i] == '?':
        		stack.pop() if expression[i-1] == 'F' else stack.pop(-2)
        		i -= 1
        	elif expression[i] != ':':
        		stack.append(expression[i])
        	i -= 1

        return stack[-1]

print Solution().parseTernary("F?1:T?4:5")
