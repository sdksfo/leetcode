"""
Requirement:

Reverse a linked list from position m to n. Do it in one-pass.

Approach:

1) Iterate through the LL from left until 'm' is reached.
2) From 'm' until 'n' reverse the nodes like in typical LL reversal
3) Keep track of the prev_node for m and next_node for n, as after reversal it becomes prev_node for n and next_node for m respectively.

Complexity:

Time: O(n) Space: O(1)
"""

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy_head, m = ListNode(None), m-1
        prev_node_for_m, dummy_head.next = dummy_head, head

        for _ in range(m):
            prev_node_for_m = head
            head = head.next

        m_node, temp, prev = head, None, head

        for _ in range(n-m):
            n_node = head
            head = head.next
            prev.next = temp
            temp, prev = prev, head

        prev_node_for_m.next, m_node.next = n_node, head

        return dummy_head.next
