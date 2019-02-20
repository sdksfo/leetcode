
"""
If node has a right sub-tree search to the left of the right sub-tree
Else climb up the parents, until a parent has a value greater than current node
"""

class Solution(object):
    def inorderSuccessor(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        val = node.val
        if node.right:
            node = node.right
            while node.left:
                node = node.left
        else:
            while node and node.val <= val:
                node = node.parent
        return node
