
"""
First create an adjacency list for the pre-requisites and courses and then detect if there is a cycle using DFS.

For detecting cycle, we check if the current neighbor is part of the recursion stack, which indicates a loop
"""

class Solution(object):
    def canFinish(self, courses, pre_req):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adjacency_list, visited = {course: [] for course in xrange(courses)}, set()

        for req in pre_req:
            adjacency_list[req[0]].append(req[1])

        def check_loop(node, stack, visited):
            if node in stack:
                return False
            if node in visited:
                return True
            stack.add(node), visited.add(node)
            result = all([check_loop(neighbor, stack, visited) for neighbor in adjacency_list[node]])
            stack.remove(node)
            return result

        for node in adjacency_list:
            if not check_loop(node, set(), visited):
                return False
        return True

print Solution().canFinish(4, [[0,1],[0,2],[1,2],[1,0]])
