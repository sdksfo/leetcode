"""
Every digit that gets added to the sequence adds 'n' more possibilities to the output where 'n' is the offset from 3.

e.g For 3 elements, we have 1 sub-array [1,2,3] ending with 3
For 4 elements [1,2,3,4] we have [1,2,3,4], [2,3,4] ie it adds 2 new sub-arrays ending with 4.
For 5 elements [1,2,3,4,5], we have [1,2,3,4,5], [2,3,4,5], [3,4,5] ie it adds 3 new sub-arrays ending with 5.
Likewise for 6 elements, we will have 4 new sub-arrays that'd be added, so on and forth.

TLDR:

So the logic is to add 1 for every single element that gets added in the sequence from size of 3.

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
