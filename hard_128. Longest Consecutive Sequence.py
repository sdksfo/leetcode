
"""
For each number check if its predecessor and successor is in the same group ie with the same parent
using UnionFind
"""
import sys

class Solution(object):
    def union(self, u, v):
        self.parent[u] = v

    def getParent(self, u):
        if self.parent[u] != sys.maxint:
            return self.getParent(self.parent[u])
        return u

    def countMaxChild(self, nums):
        self.count = {num:0 for num in nums}
        for num in self.parent:
            self.count[self.getParent(num)] += 1
        return max(self.count.values() if self.count else [0])

    def longestConsecutive(self, nums):
        self.parent = {num:sys.maxint for num in nums}
        for num in nums:
            parent_1 = parent_2 = None
            if num-1 in self.parent:
                parent_1 = self.getParent(num-1)
            if num+1 in self.parent:
                parent_2 = self.getParent(num+1)
            if parent_1 and parent_2 and parent_1 != parent_2:
                self.union(parent_1, parent_2)
            if (parent_1 or parent_2) and num not in (parent_1, parent_2):
                self.union(num, parent_1 or parent_2)
        return self.countMaxChild(nums)

print Solution().longestConsecutive([0,-1])
