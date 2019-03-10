# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        nodes, new_head = {}, None

        def getOrCopyNode(node):
            if node not in nodes:
                nodes[node] = Node(node.val, None, None)
            return nodes[node]

        while head:
            new_node = getOrCopyNode(head)
            if head.random:
                new_random_node = getOrCopyNode(head.random)
                new_node.random = new_random_node
            if head.next:
                new_next_node = getOrCopyNode(head.next)
                new_node.next = new_next_node
            new_head = new_head or new_node
            head = head.next
        return new_head


print Solution().copyRandomList(n1)
