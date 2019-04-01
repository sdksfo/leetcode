import itertools


class Solution(object):
    def getIslandCoordinates(self, grid, rows, cols, row, col, visited):
        output = []
        queue = [[row, col]]
        while queue:
            row, col = queue.pop(0)
            output.append((row, col))
            for r, c in (row+1, col), (row-1, col), (row, col+1), (row, col-1):
                if r not in (-1, rows) and c not in (-1, cols) and grid[r][c] and (r, c) not in visited:
                    visited.add((r, c))
                    queue.append([r, c])
        return output

    def getMinSteps(self, islands, grid, rows, cols):
        small_island = min(islands, key=len)
        queue, visited, steps = small_island + [None], set(small_island), 0
        while queue:
            node = queue.pop(0)
            if node:
                row, col = node
                for r, c in (row+1, col), (row-1, col), (row, col+1), (row, col-1):
                    if r not in (-1, rows) and c not in (-1, cols) and (r, c) not in visited:
                        if grid[r][c]: return steps
                        visited.add((r,c))
                        queue.append((r,c))
            else:
                steps += 1
                queue.append(None) if queue else None

    def shortestBridge(self, grid):
        if not grid or not grid[0]: return None
        rows, cols, visited, islands = len(grid), len(grid[0]), set(), []
        for row, col in itertools.product(range(rows), range(cols)):
            if (row, col) not in visited and grid[row][col]:
                islands.append(self.getIslandCoordinates(grid, rows, cols, row, col, visited))
        return self.getMinSteps(islands, grid, rows, cols)
