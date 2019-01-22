
# Explanation

# T[0, 5] = palindrome if T[0] == T[5] and dp[1,4] is also palindrome

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[0 for i in xrange(len(s))] for i in xrange(len(s))]

        for i in xrange(len(s)): dp[i][i] = 1

        for row in xrange(len(s)-2, -1, -1):
        	for col in xrange(row+1, len(s)):
        		if s[row] == s[col]:
        			if row + 1 == col: # substring of length 2
        				dp[row][col] = 1
        			else:
        				dp[row][col] = 1 if dp[row+1][col-1] > 0 else 0

        return sum([sum(i) for i in dp])

print Solution().countSubstrings('abbded')
