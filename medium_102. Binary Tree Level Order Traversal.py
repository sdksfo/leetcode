
# Explanation

# Do a BFS of the tree by using a queue and null to separate each levels.

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        outer, inner, roots = [], [], [root, None]
        while roots:
        	root = roots.pop(0)
        	if root:
        		inner.append(root.val)
        		roots.extend(filter(lambda x: x, [root.left, root.right]))
        	else:
        		outer.append(inner)
        		inner = []
        		roots.append(None) if roots else roots
        return outer

print Solution().levelOrder(node1)
