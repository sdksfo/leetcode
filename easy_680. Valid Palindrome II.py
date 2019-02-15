
"""
Use two pointers, if strings don't match, remove i and j and see if any thing returns a palindrome
"""

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1

        while i < j:
          if s[i] == s[j]:
              i += 1
              j -= 1
          elif s[i] != s[j]:
              return (s[:i] + s[i+1:]) == (s[:i] + s[i+1:])[::-1] or (s[:j] + s[j+1:]) == (s[:j] + s[j+1:])[::-1]
        return True
