
"""
Every digit that gets added to the sequence adds 'n' more possibilities to the output where 'n' is the difference between number of digits in array and 3.

e.g For [1,2,3] we have [1,2,3]
For [1,2,3,4] we have [1,2,3], [1,2,3,4], [2,3,4] ie it adds 2 new sub-arrays ending with 4.
For [1,2,3,4,5], we have [1,2,3,4,5], [2,3,4,5], [3,4,5] ie it adds 3 new sub-arrays ending with 5 to whatever we could make with 4 elements ie [1,2,3,4]

"""

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp, seq_count = [0 for i in xrange(len(A))], 0

        for i in xrange(2, len(A)):
        	if A[i] - A[i-1] == A[i-1] - A[i-2]:
        		seq_count += 1
        		dp[i] = seq_count
        	else:
        		seq_count = 0

        return sum(dp)

print Solution().numberOfArithmeticSlices([1, 2, 3, 4, 5, 6])
