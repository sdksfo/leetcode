"""
Saddleback search algorithm:

Start from top right element

If element == number, return True
If element is greater than number, move left
If element is lesser than number, move down
If out of bounds return False

Complexity: O(m+n)
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False

        rows, cols = len(matrix), len(matrix[0])

        def search(r, c):
        	if r in (-1, rows) or c in (-1, cols):
        		return False
        	if matrix[r][c] == target:
        		return True
        	elif matrix[r][c] > target:
        		return search(r, c-1)
        	else:
        		return search(r+1, c)

        return search(0, cols-1)

print Solution().searchMatrix([[1,   3,  5,  7]], 7)
