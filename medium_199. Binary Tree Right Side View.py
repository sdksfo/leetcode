
# Explanation

# Do a level order traversal and add the last element in each level to the output

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

nodes = [TreeNode(i) for i in xrange(7)]
nodes[1].left = nodes[2]
nodes[1].right = nodes[3]
nodes[2].right = nodes[5]
nodes[3].right = nodes[4]


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []

        roots, output = [root, None], []

        while roots:
        	root = roots.pop(0)
        	if root:
        		right_node = root.val
        		roots.extend(filter(lambda x: x, [root.left, root.right]))
        	else:
        		roots.append(None) if roots else None
        		output.append(right_node)

        return output

print Solution().rightSideView(nodes[1])
