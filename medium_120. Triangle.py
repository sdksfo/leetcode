
# Explanation

# From top down the minimum path to any triangle is the min of paths from row above

# ie dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + dp[i][j]

# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]

# Fill the DP table like this where 'm' is maxint
# 0 0 0 0 0
# m m m 2 m
# m m 3 4 m
# m 6 5 7 m
# 4 1 8 3 m

import sys

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        max_rows = len(triangle[-1])
        dp = [[0] * (max_rows+1)] + [[sys.maxint] * (max_rows - len(triangle[i])) + triangle[i] + [sys.maxint] for i in xrange(max_rows)]
        for row in xrange(1, max_rows+1):
        	for col in xrange(max_rows):
        		dp[row][col] = min(dp[row-1][col] + dp[row][col], dp[row-1][col+1] + dp[row][col])
        return min(dp[-1])


print Solution().minimumTotal([
     [2], [3,4], [9, 0, 0]
])

