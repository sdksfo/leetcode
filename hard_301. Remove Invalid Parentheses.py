
"""

1) Try to understand how many brackets need to be removed to make this valid
2) At each level, remove one bracket at a time
3) Mark a string as visited before adding to the queue
4) Reset the visited nodes at the end of each level
5) Use a counter to keep track of number of brackets removed
6) In the final level, when the counter drops to zero, add to a set only those that are valid

"""

class Solution(object):

    def getUnbalanced(self, s):
        """Returns the number of brackets that need to be removed to make this string valid."""
        stack, counter = [], 0
        for char in s:
            if char == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    counter += 1
            if char == '(':
                stack.append(char)
        return counter + len(stack)

    def isValid(self, s):
        """checks if the string has balanced parantheses"""
        stack = []
        for char in s:
            if char == ')' and not stack:
                return False
            if char == ')':
                stack.pop()
            if char == '(':
                stack.append(char)
        return not stack

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ctr = self.getUnbalanced(s)
        if ctr == 0: return [s]
        queue = [s, None]
        visited = set()

        while queue:
            element = queue.pop(0)
            if not element:
                ctr -= 1
                if ctr and queue:
                    queue.append(None)
            else:
                for char in xrange(len(element)):
                    if element[char] == ')' or element[char] == '(':
                        new_element = element[:char]+element[char+1:]
                        if new_element not in visited:
                            queue.append(new_element)
                            visited.add(new_element)
            if ctr == 0:
                return [c for c in queue if self.isValid(c)]

print Solution().removeInvalidParentheses('()())')
