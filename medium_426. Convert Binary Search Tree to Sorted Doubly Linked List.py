"""
Solved this problem using iterative DFS inorder traversal. The actual changes are done atop the below inorder traversal code:

class Solution(object):
    def inorderTraversal(self, root):
        stack, node = [], root
        while stack or node :
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop() # retrieves the next biggest element
                node = node.right

In in-order traversal, each time a node(next bigger element) is popped, we are certain its left sub-tree is already evaluated.
We will modify the pointers at this point, ie modify the left pointer of this popped node to be the previously popped element.
"""

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        stack, node, head, prev = [], root, None, None

        def adjust_pointer(node1, node2):
            if node1:
                node1.right = node2
                node2.left = node1

        while stack or node :
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                head = head or node
                adjust_pointer(prev, node)
                prev, node = node, node.right

        adjust_pointer(prev, head)

        return head

node = Solution().treeToDoublyList(n[4])
