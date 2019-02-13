"""
Start with every node and explore all 4 directions until u hit a wall.
Mark the point as visited (by changing it to 2)
"""

class Solution(object):
    def hasPath(self, maze, start, dest):
        rows, cols = len(maze)-1, len(maze[0])-1

        def dfs(row, col):
            if [row, col] == dest:
                return True
            if maze[row][col] == 2:
                return False
            up, down, left, right = row, row, col, col
            while up > 0 and maze[up-1][col] != 1:
                up -= 1
            while down < rows and maze[down+1][col] != 1:
                down += 1
            while left > 0 and maze[row][left-1] != 1:
                left -= 1
            while right < cols and maze[row][right+1] != 1:
                right += 1
            maze[row][col] = 2
            return dfs(up, col) or dfs(down, col) or dfs(row, left) or dfs(row, right)

        return dfs(*start)

print Solution().hasPath([
[1,1,1,0,1],
[1,1,1,0,1],
[1,0,0,0,1],
[1,1,1,0,1],
[1,1,1,1,1]],
[0,3],
[3,3])
