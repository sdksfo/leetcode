

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue, output = [root, None] if root else [], [root.val] if root else []

        while queue:
            root = queue.pop(0)
            if root:
                queue.extend(filter(lambda x: x, (root.left, root.right)))
            elif queue:
                output.append(max(queue, key=lambda x: x.val).val)
                queue.append(None)

        return output
