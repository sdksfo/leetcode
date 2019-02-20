
class Node(object):
    def __init__(self, val):
        self.val = val

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')

adjacency_list = {A: [B, C], B: [D], C: [D, F], D: [E], E:[], F: [E, D]}

visited, stack = set(), []

def topo(node):
    for neighbor in adjacency_list[node]:
        if neighbor not in visited:
            topo(neighbor)
            visited.add(neighbor)
    stack.append(node)

for node in adjacency_list:
    if node not in visited:
        topo(node)
        visited.add(node)

for i in stack[::-1]:
    print i.val