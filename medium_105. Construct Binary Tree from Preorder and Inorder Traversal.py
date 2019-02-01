# Explanation

# Similar to building a BST from a sorted array, where we start from the middle of the array which
# is the root of the tree.

# Likewise, The first index of the preorder list is the root of the tree. We use this detail
# to recursively build the left sub tree and right sub tree.


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder: return
        root, tree_len = TreeNode(preorder[0]), inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:tree_len+1], inorder[:tree_len])
        root.right = self.buildTree(preorder[tree_len+1:], inorder[tree_len+1:])
        return root

Solution().buildTree([0, 3, 8, 6, 1, 4, 2, 7, 5], [3, 8, 6, 1, 4, 0, 2, 7, 5])
