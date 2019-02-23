


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue, total = [root, None] if root else [], 0

        while queue:
        	root = queue.pop(0)
        	if root:
        		queue.extend(filter(lambda x: x, [root.left, root.right]))
        		if root.left and not root.left.left and not root.left.right:
        			total += root.left.val
        	else:
        		queue.append(None) if queue else None

        return total
