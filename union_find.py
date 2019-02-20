
# https://www.geeksforgeeks.org/union-find/

from collections import defaultdict

class Graph(object):

	def __init__(self, vertices):
		self.vertices = vertices
		self.graph = defaultdict(list)
		self.parent = {i:-1 for i in xrange(self.vertices)}

	def addEdge(self, v1, v2):
		self.graph[v1].append(v2)

	def union(self, v1, v2):
		self.parent[v1] = v2

	def getParent(self, v):
		if self.parent[v] == -1:
			return v
		return self.getParent(self.parent[v])

	def isCyclic(self):
		for v1 in self.graph:
			for v2 in self.graph[v1]:
				parent_1 = self.getParent(v1)
				parent_2 = self.getParent(v2)
				if parent_1 == parent_2:
					return True
				self.union(parent_1, parent_2)
		return False


g = Graph(3)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)

print g.isCyclic()
