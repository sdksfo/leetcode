"""
Requirement:

Merge two sorted linked lists

Approach:

Use the same technique for merging as in merge sort

Complexity:

Time: O(m+n), where m and n is length of m and n respectively
Space: O(1)
"""

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node = dummy = ListNode(None)

        while l1 and l2:
            if l1.val < l2.val:
                new_node = ListNode(l1.val)
                l1 = l1.next
            else:
                new_node = ListNode(l2.val)
                l2 = l2.next
            node.next = new_node
            node = new_node

        if l1 or l2:
            node.next = l1 or l2

        return dummy.next
