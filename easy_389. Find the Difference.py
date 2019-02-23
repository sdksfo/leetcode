
"""sort the strings and use two pointer."""

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s, t, i  = sorted(s), sorted(t), 0

        while i < len(s) and s[i] == t[i]:
        	i += 1
        return t[i]

print Solution().findTheDifference('', 'e')
