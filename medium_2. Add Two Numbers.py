

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = prev = ListNode(None)
        carry = 0

        while l1 or l2 or carry:
            total = l1.val if l1 else 0 + l2.val if l2 else 0 + carry
            carry, val = divmod(total, 10)
            node = ListNode(val)
            prev.next = node
            prev = node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
