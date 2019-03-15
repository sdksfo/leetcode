
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def removeLeaf(self, root, leaves):
        if root:
            if root.left and not root.left.left and not root.left.right:
                leaves.append(root.left.val)
                root.left = None
            if root.right and not root.right.left and not root.right.right:
                leaves.append(root.right.val)
                root.right = None
            self.removeLeaf(root.left, leaves)
            self.removeLeaf(root.right, leaves)
        return leaves

    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        output = []
        if root:
            output.append([root.val])
            while root.left or root.right:
                output.append(self.removeLeaf(root, []))
        return output
