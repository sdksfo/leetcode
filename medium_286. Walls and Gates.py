
"""
Do a BFS traversal. Traverse on 0 first and add its neighbors as +1 and add the to the queue.
The neighbors will be reached in the order of their proximity to the 0, and so mark them as 0 as you see them.
"""


class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        rows, cols, visited, queue = len(rooms), len(rooms[0]) if rooms else 0, set(), []

        for row in xrange(rows):
        	for col in xrange(cols):
        		if not rooms[row][col]:
        			queue.append((row, col))
        			visited.add((row, col))

        while queue:
        	row, col = queue.pop(0)
        	for nr, nc in (row+1, col), (row-1, col), (row, col+1), (row, col-1):
        		if (nr, nc) not in visited and 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] != -1:
        			rooms[nr][nc] = rooms[row][col] + 1
        			queue.append((nr, nc))
        			visited.add((nr, nc))
