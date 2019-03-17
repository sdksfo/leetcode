
# """
# 1) Create a graph with nodes and descendants, since its a directed graph.
# 2) Do a topological sort to determine the order.
# 3) During the topological sort, use the recursive stack to determine if there is a cycle and return '' if so.
# """


class Node(object):
    def __init__(self, value):
        self.value = value
        self.neighbors = set()

class Solution(object):
    def __init__(self):
        self.graph = {}

    def createGraph(self, words):
        """creates a graph for each word"""
        self.graph, prev_word = {char: Node(char) for char in set(''.join(words))}, words[0]
        for curr_word in words[1:]:
            i = 0
            while i < len(curr_word) and i < len(prev_word):
                if prev_word[i] != curr_word[i]:
                    self.graph[prev_word[i]].neighbors.add(curr_word[i])
                    break
                i += 1
            prev_word = curr_word

    def dfs(self, char, visited, stack, output):
        """DFS of graph nodes and appends to the output list in the order of discovery"""
        if char in stack: return None
        stack.append(char)
        if char not in visited:
            visited.add(char)
            for neighbor in self.graph[char].neighbors:
                if not self.dfs(neighbor, visited, stack, output):
                    return []
            output.append(char)
        stack.pop()
        return output

    def getTopologicalOrder(self, words):
        """returns a topological ordering of the nodes in the graph"""
        self.createGraph(words)
        visited, output = set(), []
        for char in self.graph:
            if char not in visited and not self.dfs(char, visited, [], output):
                return ''
        return ''.join(output[::-1])

    def alienOrder(self, words):
        """return an order for the alien dictionary"""
        return self.getTopologicalOrder(words) if words else ''

print Solution().alienOrder(["a","b","ca","cc"])
