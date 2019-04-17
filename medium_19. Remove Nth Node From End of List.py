"""
Requirement:

Remove nth node from end of linked list

Approach:

1) Use floyd' slow and fast pointer approach
2) The slow pointer should trail the fast pointer by a distance of 'n', such that when the fast pointer reaches
   the end, the slow pointer is at 'n'th node from tail. We can then adjust the node references to remove it.

Complexity:

Time : O(n)
Space: O(1)

"""

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast_ptr = copy_head = slow_ptr = head

        while n:
        	fast_ptr = fast_ptr.next
        	n -= 1

        if not fast_ptr: # implies the first node to be removed
        	return copy_head.next

        while fast_ptr:
        	fast_ptr = fast_ptr.next
        	prev_node = slow_ptr
        	slow_ptr = slow_ptr.next

        prev_node.next = slow_ptr.next

        return copy_head
