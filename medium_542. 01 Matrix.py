
class Solution(object):
    def updateMatrix(self, grid):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols, visited, queue = len(grid), len(grid[0]) if grid else 0, set(), []

        for row in xrange(rows):
            for col in xrange(cols):
                if not grid[row][col]:
                    queue.append((row, col))
                    visited.add((row, col))
                else:
                    grid[row][col] = rows*cols

        def bfs():
            while queue:
                row, col = queue.pop(0)
                for (nr, nc) in (row-1, col), (row+1, col), (row, col+1), (row, col-1):
                    if (nr, nc) not in visited and (0 <= nr < rows) and (0 <= nc < cols):
                        grid[nr][nc] = grid[row][col] + 1
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            return grid

        return bfs()

print Solution().updateMatrix([
    [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
    [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]])
