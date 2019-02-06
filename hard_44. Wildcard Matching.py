
"""
    '?' matches single character
    '*' matches many characters
"""

class Solution(object):
    cache={}
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if (s, p) in self.cache:
            return self.cache[(s,p)]

        if (s == p) or (p and p == '*'*len(p)):
            return True

        if not s or not p:
            return False

        if s[0] == p[0]:
            self.cache[(s,p)] = self.isMatch(s[1:], p[1:])
        elif p[0] == '?':
            self.cache[(s,p)] = self.isMatch(s[1:], p[1:])
        elif p[0] == '*':
            self.cache[(s,p)] = self.isMatch(s[1:], p) or self.isMatch(s[1:], p[1:]) or self.isMatch(s, p[1:])

        return self.cache.get((s,p), False)

print Solution().isMatch("a", "a*")
