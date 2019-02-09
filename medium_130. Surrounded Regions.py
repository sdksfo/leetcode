"""
For every 0 that is encountered, do a DFS and then if it connects to a border, do not flip to 'X'. Else change to 'X'
"""

class Solution(object):
    def solve(self, grid):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        rows, cols, seen = len(grid), len(grid[0]) if grid else 0, {}

        def dfs(row, col):
        	if row not in (-1, rows) and col not in (-1, cols) and grid[row][col] == 'O':
        		seen.add((row, col))
        		if row in (0, rows-1) or col in (0, cols-1) or dfs(row+1, col) or dfs(row, col+1) or dfs(row-1, col) or dfs(row, col-1):
        			return True
        		grid[row][col] = 'X'
        	return False

        for row in xrange(rows):
        	for col in xrange(cols):
        		if grid[row][col] == 'O':
        			dfs(row, col)

        # for i in grid:
        for i in grid:
        	print i, '\n'
        print grid
        print [["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]]

# print Solution().solve([
# 	['X', 'X', 'X', 'X'],
# 	['X', '0', '0', 'X'],
# 	['X', 'X', '0', 'X'],
# 	['X', '0', '0', 'X'],
# 	])

# print Solution().solve(
# 	[["X","X","X","X"],
# 	 ["X","O","O","X"],
# 	 ["X","X","O","X"],
# 	 ["X","O","X","X"]]
# )

print Solution().solve(
	[["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]]
)

