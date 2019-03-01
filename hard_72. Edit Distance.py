"""
Given two strings s and d, for any suffix i and j of s and d respectively,

dp[i][j] = 1 + min(replacing x[i] with y[j], 1 + inserting j before suffix y[j:], 1 + deleting i in suffix x[i:])

"""
class Solution(object):
    cache = {}
    def minDistance(self, s, d):
        if not s or not d:
            return max(len(s), len(d))
        if (s, d) not in self.cache:
            if s[0] == d[0]:
                self.cache[(s,d)]  = self.minDistance(s[1:], d[1:])
            else:
                self.cache[(s,d)]  = 1  + min(self.minDistance(s[1:], d[1:]), self.minDistance(s, d[1:]), self.minDistance(s[1:], d))
        return self.cache[(s, d)]

print Solution().minDistance('intention', 'execution')
