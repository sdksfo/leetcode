
"""Add to a stack for every element read, and if a backspace is encountered pop from stack if it has value"""

class Solution(object):
    def processString(self, s):
        stack = []
        for char in s:
            if char == '#':
                stack.pop() if stack else None
            else:
                stack.append(char)
        return ''.join(stack)

    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.processString(S) == self.processString(T)

print Solution().backspaceCompare('a#c', 'b')
