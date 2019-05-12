# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or (not root.left and not root.right): return root
        
        stack, prev, head = [], None, None

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if prev: 
                    head = head or prev
                    prev.left, prev.right = None, root
                prev, root = root, root.right
        
        prev.left = prev.right = None
        
        return head
