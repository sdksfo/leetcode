

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        stack = []

        while stack or root:
        	if root:
        		stack.append(root)
        		root = root.left
        	else:
        		root = stack.pop()
        		if root.val >= val: return root if root.val == val else None
        		root = root.right
