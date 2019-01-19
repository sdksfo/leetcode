

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [1] + [0] * len(s)

        for i in xrange(len(s)):
        	dp[i+1] = 0 if s[i] == '0' else dp[i]
        	if i > 0 and 9 < int(s[i-1:i+1]) < 27:
        		dp[i+1] += dp[i-1]

        return dp[-1]

print Solution().numDecodings('12')