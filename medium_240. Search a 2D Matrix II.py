"""
Similar to saddleback algorithm, we start at the first row and last col. We have both rows and cols sorted,
so we can use that property, to determine the following:

a) If matrix[row][col] < target: we can eliminate the row and process the next row
b) If matrix[row][col] > target: This implies our element could lie in that row. But we can completely eliminate the last
column since the col is also sorted.

Complexity: O(m+n), since traversal happens 'm' rows at most and we could potentially do at most 'n' scans in column.
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows, cols = len(matrix), len(matrix[0]) if matrix else 0

        r, c = 0, cols-1

        while r < rows and c > -1:
            if matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            elif matrix[r][c] == target:
                return True

        return False

print Solution().searchMatrix([[2,5,8,12,19]], 5)
