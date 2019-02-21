
"""
The redundant connection is one that forms the cycle. If we use Union-Find to find the
edge that has the same parents or ie. the one that forms the cycle, the edge can be returned
as the redundant edge
"""

class Solution(object):
    def getParent(self, v):
        if v in self.parent:
            return self.getParent(self.parent[v])
        return v
    def findRedundantConnection(self, edges):
        self.parent = {}
        for u, v in edges:
            parent_1 = self.getParent(u)
            parent_2 = self.getParent(v)
            if parent_1 == parent_2:
                return [u, v]
            self.parent[parent_1] = parent_2
        return []

print Solution().findRedundantConnection([[1,4], [1,2], [2,3], [3,4], [1,5]])
