
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, output = [], []

        while stack or root:
        	if root:
        		stack.append(root)
        		output.append(root.val)
        		root = root.left
        	else:
        		root = stack.pop()
        		root = root.right

        return output
