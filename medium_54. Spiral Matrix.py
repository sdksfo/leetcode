"""
Requirement:

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Approach:

1) Pop the first row in the matrix
2) Pop the last col in the matrix for all rows
3) Pop the last row in the matrix (and reverse it)
4) Pop the first col in the matrix for all rows (and reveres it)

Complexity:

Time: I'd like to say O(rows*cols), but the pop(0) causes a array shifting which is expensive
Space: O(1)
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        output = []
        while matrix:
        	output.extend(matrix.pop(0))
        	if matrix and matrix[0]:
        		output.extend(i.pop() for i in matrix)
        	if matrix and matrix[0]:
        		output.extend(matrix.pop()[::-1])
        	if matrix and matrix[0]:
        		output.extend([i.pop(0) for i in matrix][::-1])
        return output

matrix = [
 [ 1, 2, 3, 4, 5 ],
 [ 6, 7, 8, 9, 10],
 [ 11, 12, 13, 14, 15],
 [ 16, 17, 18, 19, 20],
 [ 21, 22, 23, 24, 25],
 [ 26, 27, 28, 29, 30]
]

matrix = [[7], [9], [6]]

print Solution().spiralOrder(matrix)
