


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        array, stack = [], []

        while head:
        	array.append(head.val)
        	head = head.next

        output = [0] * len(array)

        for i, d in enumerate(array):
        	while stack and array[stack[-1]] < d:
        		output[stack[-1]] = d
        		stack.pop()
        	stack.append(i)

        return output
