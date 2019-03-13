class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def lca(root, p, q):
            if root:
                if (root.val >= p.val and root.val <= q.val):
                    return root
                return lca(root.left, p, q) if root.val > p.val and root.val > q.val else lca(root.right, p, q)

        return lca(root, *sorted((p, q), key=lambda x: x.val))
