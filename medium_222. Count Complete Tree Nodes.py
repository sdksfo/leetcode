
# Explanation:

# Probably a better way since this is a medium question

# But i just did a inorder traversal to get the count O(n)

class Solution(object):
    count = 0
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            self.countNodes(root.left)
            self.count += 1
            self.countNodes(root.right)
        return self.count

print Solution().countNodes(nodes[0])
