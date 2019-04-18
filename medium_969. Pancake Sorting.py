"""
Approach:

At each step try to move the largest number in the sub-array to the right most point

Complexity:

Time: O(n**2) Space: O(1)
"""

class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        output = []

        for i in xrange(len(A)-1, -1, -1):
        	num = i+1
        	maxi = A.index(num)
        	A = A[:maxi+1][::-1] + A[maxi+1:]
        	output.append(maxi+1)
        	A = A[:i+1][::-1] + A[i+1:]
        	output.append(i+1)

        return output
