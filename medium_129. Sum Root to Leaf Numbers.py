"""
Approach:

Sum at a node is : prev_sum * 10 + node.val

a) If there is a leaf node, return prev_sum * 10 + node.val
b) If there is a left path, recursively compute the left sub tree
c) If there is a right path, recursively compute the right sub tree
"""

class Solution(object):
    def sumNumbers(self, root, s=0):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            if not root.left and not root.right:
                return s*10 + root.val
            else:
                return self.sumNumbers(root.left, s*10+root.val) + self.sumNumbers(root.right, s*10+root.val)
        return 0

print Solution().sumNumbers(n[0])
