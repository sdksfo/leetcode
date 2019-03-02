
"""

Given a string s and a string t, check if s is subsequence of t.

There are multiple ways to solve this problem.

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

"""

"""

Solution 1:

Using the two pointer technique, while chars are equal, move the pointers on both the t string and s string else just s.

"""


# class Solution(object):
#     def isSubsequence(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         i = j = 0

#         while i < len(s) and j < len(t):
#           if s[i] == t[j]:
#               i += 1
#           j += 1

#         return i == len(s)

# print Solution().isSubsequence('ak', 'ahbgdc')


"""

Solution 2:

Using DP.
#
Recurrence:

if s[i] == t[j]:
    dp[i][j] = dp[i+1][j+1]
else:
    dp[i][j] = dp[i+1][j]
"""


class Solution(object):
    cache = {}
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s :
            return True
        if not t:
            return False
        if (s, t) not in self.cache:
            if s and t:
                if s[0] == t[0]:
                    self.cache[(s, t)] = self.isSubsequence(s[1:], t[1:])
                else:
                    self.cache[(s, t)] = self.isSubsequence(s, t[1:])
        return self.cache[(s, t)]

print Solution().isSubsequence('akyz', 'ahbgdclkekdsfajdslfjdlsfjsdlykjejrlejrkwjroekz')
