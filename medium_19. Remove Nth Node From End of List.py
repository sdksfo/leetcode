
"""
Send two pointers slow and fast pointers at spacing of 'n' between them.
When the fast pointer reaches the end of the list, the second pointer is at the
'n' th element.
"""

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow, fast = head, head

        while n:
        	fast = fast.next
        	n -= 1

        if not fast:
        	head = head.next
        	return head

        while fast:
        	fast = fast.next
        	prev = slow
        	slow = slow.next

        if slow.next:
        	slow.val = slow.next.val
        	slow.next = slow.next.next
        else:
        	prev.next = None

        return head
