

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
        	return 0
        queue, depth = [root, None] if root else [], 1
        while queue:
        	root = queue.pop(0)
        	if root:
        		if root.left:
        			queue.append(root.left)
        		if root.right:
        			queue.append(root.right)
        		if not root.left and not root.right:
        			return depth
        	else:
        		queue.append(None) if queue else None
        		depth += 1
