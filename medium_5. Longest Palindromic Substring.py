
"""
Solved with dynamic programming.

For every substring s[i:j],

a) dp[i][j] = 0 if s[i] != s[j]

b) dp[i][j] = 2 + dp[i+1][j-1] if s[i+1:j-1] is a palindrome

"""
class Solution(object):
    def longestPalindrome(self, s):
        dp, max_len, max_palin = [[0 for i in xrange(len(s))] for i in xrange(len(s))], 0, s[0] if s else ''

        for i in xrange(len(s)):
            dp[i][i] = 1

        for i in xrange(len(s)-2, -1, -1):
            for j in xrange(i+1, len(s)):
                if s[i] == s[j]:
                    if dp[i+1][j-1]:
                        dp[i][j] = 2 + dp[i+1][j-1]
                    if i+1==j: # substring of length 2
                        dp[i][j] = 2
                    if dp[i][j] > max_len:
                        max_palin = s[i:j+1]
                        max_len = dp[i][j]
        return max_palin


print Solution().longestPalindrome('abcdde')
