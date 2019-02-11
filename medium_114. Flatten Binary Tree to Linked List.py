

"""
Store the pre-order traversal of the tree in a list and adjust the pointers.

There is probably a better solution to modify the pointers, without using an extra  array.
"""
class Solution(object):
    nodes = []
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if root:
                self.nodes.append(root)
                dfs(root.left)
                dfs(root.right)
            return self.nodes
        nodes = dfs(root)
        for i in xrange(1, len(nodes)):
            nodes[i-1].left, nodes[i-1].right = None, nodes[i]
        nodes[-1].right = None
