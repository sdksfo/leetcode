"""
For every O that is encountered, do a BFS and then if it connects to a border, do not flip to 'X'. Else change to 'X'.

During the course of BFS, we do not know yet if its connected to a border and so we maintain a boolean `border_found` and
also keep track of all the 0's in the grid thats connected to the border.
"""

class Solution(object):
    def solve(self, grid):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        rows, cols, seen = len(grid), len(grid[0]) if grid else 0, set()

        def bfs(row, col):
        	queue, curr_seen, border_found = [(row, col)], set(), False
        	while queue:
        		row, col = queue.pop(0)
        		if row not in (-1, rows) and col not in (-1, cols) and grid[row][col] == 'O' and (row, col) not in seen:
        			seen.add((row, col)), curr_seen.add((row, col))
        			border_found = border_found or row in (0, rows-1) or col in (0, cols-1)
        			queue.extend([(row+1, col), (row-1, col), (row, col-1), (row, col+1)])
        	if not border_found:
        		for (row, col) in curr_seen:
        			grid[row][col] = 'X'

        for row in xrange(rows):
        	for col in xrange(cols):
        		if grid[row][col] == 'O' and (row, col) not in seen:
        			bfs(row, col)

print Solution().solve(
	[["X","X","X","O","X","O","X"],
	 ["X","O","X","O","X","O","O"],
	 ["X","X","X","X","X","X","O"],
	 ["X","X","X","X","O","X","O"],
	 ["X","X","X","X","X","X","O"],
	 ["X","X","X","X","X","X","X"],
	 ["O","X","X","O","O","O","X"]]
)

