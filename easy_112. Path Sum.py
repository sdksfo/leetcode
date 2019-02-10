
class Solution(object):
    def hasPathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
        	return False
        if not root.left and not root.right and root.val == s:
        	return True
        return self.hasPathSum(root.left, s-root.val) or self.hasPathSum(root.right, s-root.val)
