
"""
Parse through the string and when a space is encountered and prev_char is not space, add 1
"""

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        ctr, s, prev = 0, s.strip(), None
        if s:
            ctr += 1
            for char in s:
                if char == ' ' and prev != ' ':
                    ctr += 1
                prev = char
        return ctr

print Solution().countSegments("Hello,   Nanny")
