

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
