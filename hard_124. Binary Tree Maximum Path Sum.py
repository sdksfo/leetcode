
"""
Rules:

There could be negative integers in the tree
The maximum path sum need not go through the root

Understanding:

For each node, the maximum sum is any of the following:

a) root + left subtree
b) root + right subtree
c) root + left subtree + right subtree
d) root (since just one node can make the path)

Approach:

For each node, do a recursive computation for all of the above conditions, and keep track
of the maximum sum, comparing against previous maximum found.

"""

class Solution(object):
    total_max = float("-inf")
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0
            lsum, rsum = dfs(root.left), dfs(root.right)
            self.total_max = max(root.val, lsum+root.val, rsum+root.val, lsum+rsum+root.val, self.total_max)
            return max(root.val, lsum+root.val, rsum+root.val)
        dfs(root)
        return self.total_max

print Solution().maxPathSum(nodes[0])
