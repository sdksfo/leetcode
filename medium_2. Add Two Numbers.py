
"""
Compute the sum of the two linked list and create a new linked list
"""

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def get_num(node, power=0):
        	if node:
	        	return (node.val *(10**power)) + get_num(node.next, power+1)
	        return 0

        def create_list(result):
        	prev = head = None
        	while result:
        		node = ListNode(result%10)
        		if prev:
        			prev.next = node
        		head = head or node
        		prev = node
        		result = result/10
        	return head or ListNode(0)

        return create_list(get_num(l1) + get_num(l2))

node = Solution().addTwoNumbers(node2, node5)
