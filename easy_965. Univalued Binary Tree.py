

class Solution(object):
    def isUnivalTree(self, node):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, prev, root_val = [], None, node.val if node else node

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if node.val != root_val: return False
                node = node.right

        return True
