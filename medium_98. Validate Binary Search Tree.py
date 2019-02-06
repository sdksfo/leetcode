
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

nodes = [TreeNode(i) for i in xrange(21)]

nodes[1].left = TreeNode(1)
nodes[10].right = nodes[15]
nodes[15].left = nodes[6]
nodes[15].right = nodes[20]


class Solution(object):
    prev, valid = None, True
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root and self.valid:
            self.isValidBST(root.left)
            self.valid = False if self.prev != None and root.val <= self.prev else self.valid
            self.prev = root.val
            self.isValidBST(root.right)
        return self.valid

print Solution().isValidBST(nodes[1])
