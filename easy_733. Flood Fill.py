
"""Do a DFS of the matrix by recursively colouring all the 4 directions"""

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        rows, cols = len(image), len(image[0]) if image else 0

        def fill(row, col, oldcolor, newcolor):
        	if row in (-1, rows) or col in (-1, cols):
        		return
        	if image[row][col] == oldcolor:
        		image[row][col] = newColor
        		fill(row+1, col, oldcolor, newcolor)
        		fill(row-1, col, oldcolor, newcolor)
        		fill(row, col-1, oldcolor, newcolor)
        		fill(row, col+1, oldcolor, newcolor)

        if image and image[sr][sc] != newColor:
        	fill(sr, sc, image[sr][sc], newColor)
        return image

print Solution().floodFill([[0,0,0],[0,1,1]], 1, 1, 1)
