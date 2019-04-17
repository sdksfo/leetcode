"""
Requirement:

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

Approach:

a) Set two dummy nodes, odd and even ptr
b) Iterate through the linked list
c) If curr_node is odd, point the next node for odd ptr at curr_node
d) If curr_node is even, point the next node for even ptr at curr_node
e) At the end of traversal, you have two lists, one with all odd nodes and another with even nodes
   Point the end of odd list to beginning of even list.
   Point the end of even list to null.

Complexity:

Time: O(n) Space: O(1)
"""

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None

        odd_ptr, even_ptr = ListNode(None), ListNode(None)
        even_start, odd_start, odd_end, even_end, odd = even_ptr, odd_ptr, head, head, True

        while head:
        	if odd:
        		odd_ptr.next = head
        		odd_ptr = odd_end = head
        	else:
        		even_ptr.next = head
        		even_ptr = even_end = head
        	head = head.next
        	odd = not odd

        odd_end.next = even_start.next
        even_end.next = None

      	return odd_start.next
