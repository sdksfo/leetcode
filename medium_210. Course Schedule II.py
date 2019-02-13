
"""
Do a topological ordering with checking for loops
"""

class Solution(object):
    def findOrder(self, courses, pre_req):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adjacency_list, visited, loop, order = {course: [] for course in xrange(courses)}, set(), False, []

        for req in pre_req:
            adjacency_list[req[0]].append(req[1])

        def dfs(node, stack):
            if node in stack:
                return True
            stack.add(node)
            if node not in visited:
                visited.add(node)
                if any(dfs(neighbor, stack) for neighbor in adjacency_list[node]):
                    return True
                order.append(node)
            stack.remove(node)

        def topological_sort():
            for node in adjacency_list:
                if node not in visited:
                    if dfs(node, set()):
                        return []
            return order

        return topological_sort()

print Solution().findOrder(2, [[0,1],[1,0]])
