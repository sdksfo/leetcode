

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, temp = 0, head

        while head:
        	prev = (prev*10) + head.val
        	head = head.next

        prev, head = str(prev+1), temp

        for char in prev:
        	if not head:
        		head = ListNode(int(char))
        		prev_node.next = head
        	else:
        		head.val = int(char)
        	prev_node = head
        	head = head.next

        return temp
