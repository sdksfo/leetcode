"""
dp[i] = max(1 + dp[i+1] if dp[i] is included, dp[i+1] if dp[i] is excluded)

Note: You only include it if the string at index i has max m 0's and n 1's
"""

class Solution(object):
    cache = {}
    def findMaxForm(self, strs, m, n, d=0):
        if (m, n, d) not in self.cache:
            if (not strs) or (not m and not n):
                return 0
            curr_m, curr_n = strs[0].count('0'), strs[0].count('1')
            if curr_m <= m and curr_n <= n:
                self.cache[m,n,d] = max(1 + self.findMaxForm(strs[1:], m-curr_m, n-curr_n, d+1), self.findMaxForm(strs[1:], m, n, d+1))
            else:
                self.cache[m,n,d] = self.findMaxForm(strs[1:], m, n, d+1)
        return self.cache[m,n,d]
