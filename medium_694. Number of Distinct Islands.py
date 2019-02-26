class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols, seen, visited = len(grid), len(grid[0]), set(), set()

        def dfs(row, col, path):
            if row < 0 or row > rows-1 or col < 0 or col > cols-1 or not grid[row][col]:
                return
            grid[row][col] = 0
            path.append('d'), dfs(row+1, col, path)
            path.append('u'), dfs(row-1, col, path)
            path.append('r'), dfs(row, col+1, path)
            path.append('l'), dfs(row, col-1, path)

        for row, col in itertools.product(xrange(rows), xrange(cols)):
            if grid[row][col]:
                path = []
                dfs(row, col, path)
                seen.add(''.join(path))

        return len(seen)
