

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue, leaf, left_found = [root, None], root, False

        while queue:
        	root = queue.pop(0)
        	if root:
        		if not left_found:
        			leaf = root
        			left_found = not left_found
        		queue.extend(filter(lambda x: x , (root.left, root.right)))
        	else:
        		left_found = not left_found
        		queue.append(None) if queue else None

        return leaf.val
