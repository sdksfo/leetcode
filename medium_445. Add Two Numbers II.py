
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

head1 = ListNode(7)
head1.next = ListNode(2)
head1.next.next = ListNode(4)
head1.next.next.next = ListNode(3)

head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(4)

class Solution(object):

    def get_number(self, head):
        val = 0
        while head:
            val = (val*10) + head.val
            head = head.next
        return val

    def get_linkedlist(self, num):
        if num:
            prev_node = None
            while num:
                new_node = ListNode(num%10)
                new_node.next = prev_node
                prev_node = new_node
                num /= 10
            return new_node
        else:
            return ListNode(0)

    def addTwoNumbers(self, l1, l2):
        total = self.get_number(l1) + self.get_number(l2)
        return self.get_linkedlist(total)


node = Solution().addTwoNumbers(head1, head2)

while node:
    print node.val
    node = node.next