
#  1->2->3->4->5->6->7->8
#   k = 3
#  3->2->1->6->5->4->8->7

"""
a) Traverse through the linked-list until n == k, adding nodes to a stack
b) Once n becomes 'k', reset n to 0
c) Pop from stack and keep reversing them

"""

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def reverseKGroup(self, node, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        stack = []
        prev = dummy_node = ListNode(None)
        while node:
            stack.append(node)
            node = node.next
            if len(stack) == k:
                while stack:
                    prev.next = stack.pop()
                    prev = prev.next
        while stack:
            prev.next = stack.pop(0)
            prev = prev.next
        prev.next = None
        return dummy_node.next
