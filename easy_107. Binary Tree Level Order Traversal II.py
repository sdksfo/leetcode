


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        output = []

        queue, temp = [root, None] if root else [], []

        while queue:
        	root = queue.pop(0)
        	if root:
        		queue.extend(filter(lambda x:x, [root.left, root.right]))
        		temp.append(root.val)
        	else:
        		queue.append(None) if queue else None
        		output.insert(0, temp)
        		temp = []

        return output
