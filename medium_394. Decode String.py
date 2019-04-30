

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for char in s:
        	if char == ']':
        		coeff, temp = '', ''
        		while stack[-1] != '[':
        			temp = stack.pop() + temp
        		stack.pop()
        		while stack and stack[-1].isdigit():
        			coeff = stack.pop() + coeff
        		stack.append(temp*int(coeff) if coeff else temp)
        	else:
        		stack.append(char)

        return ''.join(stack)

print Solution().decodeString("3[a]2[b3[acdf]]")
