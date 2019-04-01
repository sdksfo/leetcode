# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not isinstance(head, ListNode):
            return None

        dummy_head = prev_node = ListNode(None)

        while head:
            curr_node, next_node = head, head.next
            if not next_node:
                prev_node.next = curr_node
                return dummy_head.next
            prev_node.next = next_node
            temp = next_node.next
            next_node.next = curr_node
            prev_node = curr_node
            head = temp

        prev_node.next = None

        return dummy_head.next
