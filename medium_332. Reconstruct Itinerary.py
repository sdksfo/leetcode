
"""
a) Create an adjacency list and start from JFK and do a DFS
b) Sort the adjacency list for lexicographical order
c) If there exists a path, covering all the edges, then output the path
"""

import collections
import copy

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        edges = collections.defaultdict(list)
        edge_count = 0

        for src, dest in tickets:
            edges[src].append(dest)
            edge_count += 1

        for src, dest in edges.items():
            dest[:] = sorted(dest)

        def dfs(src, output, tickets):
            if sum([len(filter(lambda x: x, tickets[m])) for m in tickets]) == 0:
                return output

            for idx, dest in enumerate(tickets[src]):
                tickets[src][idx] = None
                if dfs(dest, output, copy.deepcopy(tickets)):
                    output.insert(0, dest)
                    return output
                else:
                    tickets[src][idx] = dest
            return []

        paths = dfs('JFK', ['JFK'], edges)

        return [paths[-1]] + paths[:-1]
