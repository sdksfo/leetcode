
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root:
        	return 1 + max([0] + [self.maxDepth(i) for i in root.children])
        return 0
