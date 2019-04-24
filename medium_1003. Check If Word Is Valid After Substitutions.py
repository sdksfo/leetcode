"""
Same as valid parenthesis problem
"""

class Solution(object):
    def isValid(self, s):
        """
        :type S: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char == 'c':
                if not stack or stack.pop() != 'b' or not stack or stack.pop() != 'a':
                    return False
            else:
                stack.append(char)
        return not stack

for string in ('cababc',):
    print Solution().isValid(string)
