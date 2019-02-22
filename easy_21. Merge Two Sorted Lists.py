# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prev, head = None, None
        while l1 or l2:
        	if l1 and l2:
        		if l1.val <= l2.val:
        			node = ListNode(l1.val)
        			l1 = l1.next
        		else:
        			node = ListNode(l2.val)
        			l2 = l2.next
        	elif l1:
        		node = ListNode(l1.val)
        		l1 = l1.next
        	elif l2:
        		node = ListNode(l2.val)
        		l2 = l2.next
        	head = head or node
        	if prev:
        		prev.next = node
        	prev = node
        return head

print Solution().mergeTwoLists(r2, r1).val
