"""
Every n that is a power of 2, will have 1 set bit. Bit count of every other number can be derived using the below logic. e.g bit count for 11 = bit count for 8 (which is the max possible power of 2 closest to 11) + bit count for 3 ie 3
"""

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp, one_idx = [0 for i in xrange(num+1)], 0

        for i in xrange(1, num+1):
        	if i & (i-1) == 0:
        		dp[i] = 1
        		one_idx = i
        	else:
        		dp[i] = dp[i-one_idx] + 1

        return dp

print Solution().countBits(9)
