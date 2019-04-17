"""
Requirement:

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Approach:

For each element check the immediate next element below.

Complexity:

Time: O(n) Space: O(1)
"""

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for row in xrange(len(matrix)-1):
        	for col in xrange(len(row)-1):
        		if matrix[row+1][col+1] != matrix[row][col]: return False

        return True
