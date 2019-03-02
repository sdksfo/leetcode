
"""
if s[0] == s[-1]:
    dp[i][j] = 2 + dp[i+1][j-1]
else:
    dp[i][j] = max(dp[i+1][j], dp[i][j-1]) # include the first character or the last character
"""


class Solution(object):
    # cache = {}
    # def longestPalindromeSubseq(self, s):
    #     if s not in self.cache:
    #         if s == s[::-1]:
    #             return len(s)
    #         if s[0] == s[-1]:
    #             self.cache[s] = 2 + self.longestPalindromeSubseq(s[1:-1])
    #         else:
    #             self.cache[s] = max(self.longestPalindromeSubseq(s[1:]), self.longestPalindromeSubseq(s[:-1]))
    #     return self.cache[s]

    def longestPalindromeSubseq(self, s):
        def search(i, j, cache):
            if i > j:
                return 0
            if i == j :
                return 1
            if (i, j) not in cache:
                if s[i] == s[j]:
                    cache[(i, j)] = 2 + search(i+1, j-1, cache)
                else:
                    cache[(i, j)] = max(search(i+1, j, cache), search(i, j-1, cache))
            return cache[(i, j)]
        return search(0, len(s)-1, {})

print Solution().longestPalindromeSubseq('abbbba')
