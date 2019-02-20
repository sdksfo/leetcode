
"""
The idea is the same as finding if there is a cycle using UnionFind
"""

class Solution(object):

    def getParent(self, vertex):
        if self.parent[vertex] == -1:
            return vertex
        return self.getParent(self.parent[vertex])

    def union(self, u, v):
        self.parent[u] = v

    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        self.parent = {i:-1 for i in xrange(n)}

        for u,v in edges:
            parent_u = self.getParent(u)
            parent_v = self.getParent(v)
            if parent_u == parent_v:
                return False
            self.union(parent_u, parent_v)

        return len(edges) == n-1 # This step determines if all components are connected or not

print Solution().validTree(4, [[0,1],[2,3]])
