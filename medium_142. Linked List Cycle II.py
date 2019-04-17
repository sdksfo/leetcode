"""
Requirement:

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Approach:

Once the cycle has been detected, send the slow_ptr to the head node (list  beginning) and traverse again. The fast and slow should meet at the intersection if
they both travel one node at a time.

Complexity:

Time: O(n) Space: O(1)
"""

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow_ptr = fast_ptr = head

        if head and head.next:
            while fast_ptr and fast_ptr.next:
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
                if fast_ptr == slow_ptr: break
            if fast_ptr == slow_ptr:
                slow_ptr = head
                while fast_ptr != slow_ptr:
                    fast_ptr = fast_ptr.next
                    slow_ptr = slow_ptr.next
                return fast_ptr
