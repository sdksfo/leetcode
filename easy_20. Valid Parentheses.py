
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hashmap, stack = {')': '(', '}':'{', ']': '['}, []

        for char in s:
        	if stack and hashmap.get(char, None) == stack[-1]:
        		stack.pop()
        	else:
        		stack.append(char)

        return not stack
