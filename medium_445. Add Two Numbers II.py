class Solution(object):
    def reverse(self, l):
        prev = temp = None
        while l:
            temp, l = l, l.next
            temp.next, prev = prev, temp
        return temp

    def addTwoNumbers(self, l1, l2):
        if not l1 and not l2: return None

        l1, l2, carry, num, i = self.reverse(l1), self.reverse(l2), 0, 0, 0

        while l1 or l2:
            total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            num += ((total%10)*(10**i))
            carry = total/10
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
            i += 1
        else:
            num += (carry * (10**i))

        if not num:
            return ListNode(num)

        head = prev = None

        while num:
            node = ListNode(num%10)
            head = head or node
            num = num/10
            if prev:
                prev.next = node
            prev = node

        return self.reverse(head)
