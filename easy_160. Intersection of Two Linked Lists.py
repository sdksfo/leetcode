"""
Requirement:

Find intersection of ttwo linked lists

Approach:

If both LLs are same length, sending a i ptr in one LL and a ‘j’ ptr in another, would make them converge at intersection point.
But if their lengths are different,  send the ‘j’ ptr once ‘i’ ptr has traversed exactly l1-l2 distance.
Then both these ptrs would converge at the intersection point.

Complexity:

Time: O(n) Space: O(n)
"""

class Solution(object):
    def getLengths(self, head):
        ctr = 0
        while head:
            ctr += 1
            head = head.next
        return ctr

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l1, l2 = self.getLengths(headA), self.getLengths(headB)

        if l1 >= l2:
            while l1 != l2:
                headA = headA.next
                l1 -= 1
        else:
            while l1 != l2:
                headB = headB.next
                l2 -= 1

        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA
