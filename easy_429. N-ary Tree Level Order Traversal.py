

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        queue, output, temp = [root, None] if root else [], [], []

        while queue:
            root = queue.pop(0)
            if root:
                temp.append(root.val)
                queue.extend([i for i in root.children])
            else:
                queue.append(None) if queue else None
                output.append(temp)
                temp = []
        return output
