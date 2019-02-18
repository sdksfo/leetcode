
"""
minimum falling path sum is the minimum needed at each step.

time complexity: O(n^2)
"""
import sys

class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """

        dp = A[0] if A else []
        rows, cols = len(A), len(A[0]) if A else 0

        for i in xrange(1, rows):
        	temp = []
        	for j in xrange(cols):
        		temp.append(min(dp[j-1] if j > 0 else sys.maxint, dp[j], dp[j+1] if j < cols-1 else sys.maxint) + A[i][j])
        	dp = temp
        return min(dp)

print Solution().minFallingPathSum([[1,9,3],[12,5,6],[7,1,9]])
