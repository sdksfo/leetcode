
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        stack, node, total, l_found = [], root, L+R, False

        while stack or node:
        	if node:
        		stack.append(node)
        		node = node.left
        	else:
        		node = stack.pop()
        		if node.val == R:
        			return total
        		if l_found:
        			total += node.val
        		l_found = l_found or node.val == L
        		node = node.right
