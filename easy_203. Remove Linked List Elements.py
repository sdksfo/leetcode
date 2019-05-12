# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        self.dh = ListNode(None)
        
        prev = self.dh
        
        while head:
            if head.val != val:
                prev.next = head
                prev = head
            head = head.next
        
        prev.next = None
        
        return self.dh.next
