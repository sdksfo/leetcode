"""
Do an inorder traversal of the BST and return the next node after P
"""
class Solution(object):
    def inorderSuccessor(self, root, p):
        stack, node, p_found = [], root, False
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if p_found: return node
                p_found = node is p
                node = node.right
