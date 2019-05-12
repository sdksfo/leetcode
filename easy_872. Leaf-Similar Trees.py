
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def getLeaves(root):
            if not root or (not root.left and not root.right):
                return [root.val] if root else []
            return getLeaves(root.left) + getLeaves(root.right)

        return getLeaves(root1) == getLeaves(root2)
