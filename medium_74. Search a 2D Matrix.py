"""
Saddleback search algorithm:

Start from top right element

If element == number, return True
If element is greater than number, move left
If element is lesser than number, move down
If out of bounds return False
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows, cols = len(matrix), len(matrix[0]) if matrix else 0

        def search(row, col):
        	if col < 0 or row == rows:
        		return False
        	if matrix[row][col] > target:
        		return search(row, col-1)
        	if matrix[row][col] < target:
        		return search(row+1, col)
        	return True

        return search(0, cols-1)
