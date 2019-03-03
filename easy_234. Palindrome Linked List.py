

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        array = []

        while head:
        	array.append(head.val)
        	head = head.next

        return array == array[::-1]
