"""
Requirement:

Given a node from a cyclic linked list which is sorted in ascending order, write a function to insert a value into the list such that it remains a cyclic sorted list.

Approach:

Iterate through the linked list and insert between two nodes based on the four rules below:

a) insert value lies between two values e.g [1, '2', 3]
b) insert value is smallest in the LL e.g ['0', 2, 4]
c) insert value is greatest in the LL e.g [2, 4, '5']
d) insert value is duplicated e.g ['3', 3, 3, 4]

Note: If we have traversed through the whole list and have not found an insertion point based on the four rules above, then insert between tail and head

Complexity:

Time: O(n) Space: O(1)
"""
class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        old_head, new_node = head, ListNode(insertVal)

        if not head: return new_node

        while head:
            next_node = head.next
            if (head.val == insertVal) or
               (head.val > insertVal < next_node.val and head.val > next_node.val) or
               (head.val < insertVal > next_node.val and head.val > next_node.val) or
               (head.val < insertVal < next_node.val and head.val < next_node.val) or
               (next_node == old_head):
                head.next = new_node
                new_node.next = next_node
                return old_head
            head = head.next
