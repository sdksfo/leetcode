
# Explanation
# In order traversal of the tree should yield the sorted order. Store the k'th value and return at end of recursion

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    count, val = 0, None
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return
        self.kthSmallest(root.left, k)
        self.count += 1
        if self.count == k:
            self.val = root.val
        self.kthSmallest(root.right, k)
        return self.val

print Solution().kthSmallest(node2, 1)
