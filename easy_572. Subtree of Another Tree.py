

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isMatching(self, s, t):
        if s and t:
            if s.val != t.val:
                return False
            return self.isMatching(s.left, t.left) and self.isMatching(s.right, t.right)
        return s is t

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        stack, node = [], s
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if node.val == t.val and self.isMatching(node, t):
                    return True
                node = node.right
        return False
