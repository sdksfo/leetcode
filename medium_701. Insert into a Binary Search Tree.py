
# Explanation

# If root is smaller than the insert value, go to the right

# If root is larger than the insert value, go to the left

# If by going left/right, no nodes are available make this insertion node as left or right node

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root.val < val:
        	if root.right:
        		self.insertIntoBST(root.right, val)
        	else:
        		root.right = TreeNode(val)
        else:
        	if root.left:
        		self.insertIntoBST(root.left, val)
        	else:
        		root.left = TreeNode(val)
        return root

root = Solution().insertIntoBST(node4, 5)
