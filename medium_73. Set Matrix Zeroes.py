"""
Requirement:

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Approach:

a) Iterate through the matrix
b) For each row that has 0's mark the entire row as 0 straightaway. Also capture the cols that has 0 for the given row
c) Iterate again and mark the cols as 0

Complexity:

Time: O(m*n), Space: O(n)
"""

import itertools

# Approach 1: O(n) space solution, where n is number of cols

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        cs, rows, cols = set(), len(matrix), len(matrix[0]) if matrix else 0

        for r in xrange(rows):
        	zero_r = False
        	for c in xrange(cols):
	        	if not matrix[r][c]:
	        		zero_r = True
	        		cs.add(c)
	        if zero_r:
	        	matrix[r] = [0] * cols

        for col in cs:
        	for row in xrange(rows):
        		matrix[row][col] = 0
