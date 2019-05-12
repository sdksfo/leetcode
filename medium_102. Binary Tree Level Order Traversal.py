# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        
        output, queue = [], [root]
        
        while queue:
            output.append([n.val for n in queue])
            queue = filter(lambda x: x, [m for n in queue for m in n.left, n.right])
        
        return output

