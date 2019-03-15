class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        hashmap, stack = {}, []

        def height(root):
            if root in hashmap: return hashmap[root]
            if root:
                hashmap[root] = 1 + max(height(root.left), height(root.right))
            return hashmap.get(root, 0)

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if abs(height(root.left) - height(root.right)) > 1:
                    return False
                root = root.right

        return True
