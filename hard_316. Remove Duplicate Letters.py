

# Approach 1: Add the current char to the stack if last element in stack is lesser than current element.
# Else pop as long as the last element can appear later in the string.

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        hashmap, stack = {d:i for i, d in enumerate(s)}, []

        for i, d in enumerate(s):
            while stack and stack[-1] > d and hashmap[stack[-1]] > i and d not in stack:
                stack.pop()
            if d not in stack:
                stack.append(d)

        return ''.join(stack)

# Approach 2: Same as approach1 but instead of presence check against stack to check if a char is added,
# we use a hashmap with boolean to determine if its added or not.

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        hashmap, stack, added = {d:i for i, d in enumerate(s)}, [], {}

        for i, d in enumerate(s):
            while stack and stack[-1] > d and hashmap[stack[-1]] > i and not added.get(d, False):
                added[stack.pop()] = False
            if not added.get(d, False):
                stack.append(d)
                added[d] = True

        return ''.join(stack)

print Solution().removeDuplicateLetters("cbcdbcabcdadefaf")
