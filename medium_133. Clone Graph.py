"""
BFS starting from root node. Create a clone/copy for each new node encountered and add it to a hashmap.
"""

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def cloneGraph(self, node):
    	queue, visited, head, hashmap = [node] if node else [], set(), node, {}

    	while queue:
    		node = queue.pop(0)
    		if node not in visited:
    			hashmap[node] = clone = hashmap.get(node, UndirectedGraphNode(node.label))
    			for neighbor in node.neighbors:
    				hashmap[neighbor] = clone_neighbor = hashmap.get(neighbor, UndirectedGraphNode(neighbor.label))
    				clone.neighbors.append(clone_neighbor)
    				if neighbor not in visited: queue.append(neighbor)
    			visited.add(node)

        return hashmap.get(head, None)
