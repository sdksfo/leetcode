"""
Requirement:

Given a linked list, determine if it has a cycle in it.

Approach:

a) Use floyd's cycle detection logic.
b) Send a fast and slow ptr with fast twice as fast as slow.
c) If there is a cycle, eventually both ptrs would converge in a node.

Complexity:

Time: O(n) Space: O(1)
"""

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast_ptr = slow_ptr = head

        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
            if fast_ptr == slow_ptr:
                return True

        return False
