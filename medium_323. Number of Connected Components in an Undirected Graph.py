
"""
Take each edge. For each vertex create the adjacency list. Start from one node and
travel down the adjacency list marking each node as visited.
"""


class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        count, visited, adj = 0, set(), {i:[] for i in xrange(n)}

        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)


        def dfs(node):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        for node in adj:
            if node not in visited:
                count += 1
                dfs(node)

        return count

print Solution().countComponents(2, [[1,0]])
