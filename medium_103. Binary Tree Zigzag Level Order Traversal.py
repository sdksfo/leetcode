
"""
Do a BFS of the tree and use a boolean to determine the direction.
"""

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue, reverse, output, temp = [root, None] if root else [], False, [], []

        while queue:
        	root = queue.pop(0)
        	if root:
        		temp.append(root.val)
        		queue.extend(filter(lambda x: x, (root.left, root.right)))
        	else:
        		queue.append(None) if queue else None
        		output.append(temp[::-1]) if reverse else output.append(temp)
        		temp = []
        		reverse = not reverse

        return output

print Solution().zigzagLevelOrder(n[1])
