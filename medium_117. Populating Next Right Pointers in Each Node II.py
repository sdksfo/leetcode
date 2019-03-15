class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        queue, prev, head = [root, None] if root else [], None, None

        while queue:
            root = queue.pop(0)
            if root:
                head = head or root
                if prev:
                    prev.next = root
                queue.extend(filter(lambda x: x, [root.left, root.right]))
            else:
                queue.append(root) if queue else None
            prev = root

        return head
