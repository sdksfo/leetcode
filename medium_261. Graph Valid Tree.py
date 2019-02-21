
"""
The idea is the same as finding if there is a cycle using UnionFind
"""

class Solution(object):
    def getParent(self, v):
        if v in self.parent:
            return self.getParent(self.parent[v])
        return v
    def validTree(self, n, edges):
        self.parent = {}
        for u, v in edges:
            parent_1 = self.getParent(u)
            parent_2 = self.getParent(v)
            if parent_1 == parent_2:
                return False
            self.parent[parent_1] = parent_2
        return len(edges) == n-1 # This step determines if all components are connected or not

print Solution().validTree(4, [[0,1],[2,3]])
