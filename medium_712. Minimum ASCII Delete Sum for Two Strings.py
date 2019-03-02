
"""
if s == d:
    return 0

if s[0] == d[0]:
    return s[1:], d[1:]
else:
    min(cost of deleting char in s + (s[1:], d), cost of deleting char in d + (s, d[1:]), cost of deleting char in d and s + s[1:], d[1:])
"""

# top down

class Solution(object):
    cache = {}
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        if s1 == s2: return 0

        if not s1 or not s2:
            return sum([ord(i) for i in s1 or s2])

        if s1+','+s2 not in self.cache:
            if s1[0] == s2[0]:
                self.cache[s1+','+s2] = self.minimumDeleteSum(s1[1:], s2[1:])
            else:
                self.cache[s1+','+s2] = min(ord(s1[0]) + self.minimumDeleteSum(s1[1:], s2), ord(s2[0]) + self.minimumDeleteSum(s1, s2[1:]))
        return self.cache[s1+','+s2]

# bottom up

# class Solution(object):
#     def minimumDeleteSum(self, s1, s2):
#         dp = [[0] * (len(s2) + 1) for _ in xrange(len(s1) + 1)]

#         for i in xrange(len(s1) - 1, -1, -1):
#             dp[i][len(s2)] = dp[i+1][len(s2)] + ord(s1[i])

#         for j in xrange(len(s2) - 1, -1, -1):
#             dp[len(s1)][j] = dp[len(s1)][j+1] + ord(s2[j])

#         for i in xrange(len(s1) - 1, -1, -1):
#             for j in xrange(len(s2) - 1, -1, -1):
#                 if s1[i] == s2[j]:
#                     dp[i][j] = dp[i+1][j+1]
#                 else:
#                     dp[i][j] = min(dp[i+1][j] + ord(s1[i]),
#                                    dp[i][j+1] + ord(s2[j]))

#         return dp[0][0]

print Solution().minimumDeleteSum("delete", "leet")
