"""
DFS along all the paths from root to leaf and check if there is a path that equals the sum.
"""

class Solution(object):
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
        	return []
        if not root.left and not root.right and root.val == s:
        	return [[s]]
        return [[root.val] + i for i in self.pathSum(root.left, s-root.val)] + [[root.val] + i for i in self.pathSum(root.right, s-root.val)]
