
"""

Each equation is a edge and each variable can be represented in graph. For each
of the equations create a graph of nodes and values.

a / b = 2.0, b / c = 3.0.

  2
a - b

 0.5
b - a

  3
b - c

 0.33
c - b

Return -1 if either the node is not in the graph or if the node is not reachable

"""

from collections import defaultdict

class Solution(object):
    def dfs(self, x, y, value, seen):
        if x in self.graph and y in self.graph:
            if x == y: return value
            seen.add(x)
            for k in self.graph[x]:
                if k not in seen:
                    val = self.dfs(k, y, value*self.graph[x][k], seen)
                    if val != -1: return val
        return float(-1)

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        self.graph = defaultdict(dict)

        for idx, data in enumerate(equations):
            x, y = data
            self.graph[x][y] = values[idx]
            self.graph[y][x] = float(1)/values[idx]

        return [self.dfs(*query, value=float(1), seen=set()) for query in queries]

print Solution().calcEquation([["x1","x2"],["x2","x3"],["x1","x4"],["x2","x5"]],  [3.0,0.5,3.4,5.6],  [["x2","x4"],["x1","x5"],["x1","x3"],["x5","x5"],["x5","x1"],["x3","x4"],["x4","x3"],["x6","x6"],["x0","x0"]])
