"""
Requirement:

Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Approach:

If input is ')' and last processed is '(' remove the '(', else add it.
If input is '(' add it.

Complexity:

Time: O(n) Space: O(n) [without stack its O(1)]
"""

# Approach 1: With stack

class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []

        for char in S:
        	if char == ')' and stack and stack[-1] == '(':
        		stack.pop()
        	else:
        		stack.append(char)

        return len(stack)

# Approach 2: Without stack but same logic

class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type S: str
        :rtype: int
        """
        l = r = 0

        for char in s:
        	if char == ')':
        		if l:
        			l -= 1
        		else:
        			r += 1
        	else:
        		l += 1

        return l + r
