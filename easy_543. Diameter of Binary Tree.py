
# Explanation

# diameter at each node = max of the left subtree height and right subtree height


class Solution(object):
    dia = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_height(root):
            if not root:
                return 0
            left_height = get_height(root.left)
            right_height = get_height(root.right)
            self.dia = max(self.dia, left_height+right_height)
            return 1 + max(left_height, right_height)
        get_height(root)
        return self.dia

print Solution().diameterOfBinaryTree(nodes[0])
