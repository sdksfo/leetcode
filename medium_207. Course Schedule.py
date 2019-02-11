
"""
First create an adjacency list for the pre-requisites and courses and then detect if there is a cycle using DFS.

For detecting cycle, we check if the current neighbor is part of the recursion stack, which indicates a loop
"""

class Solution(object):
    def canFinish(self, n, p):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj_list = {i:[] for i in xrange(n)}

        for [node, dep] in p:
            adj_list[node].append(dep)

        def has_cycle(node, visited, stack):
            visited.add(node)
            stack.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    if has_cycle(neighbor, visited, stack):
                        return True
                if neighbor in stack:
                    return True
            stack.remove(node)

        for node in xrange(n):
          if has_cycle(node, set(), set()):
              return False

        return True

print Solution().canFinish(4, [[0,1],[0,2],[1,2],[1,0]])
