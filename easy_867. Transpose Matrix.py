"""
Requirement:

Matrix transpose

Approach:

Array traversal

Complexity:

Time: O(n) Space: O(1)
"""


class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A: return A

        output = []

        for col in xrange(len(A[0])):
        	temp = [row[col] for row in A]
        	output.append(temp)

        return output
