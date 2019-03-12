

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        G, prev, connected_components = set(G), None, 0

        while head:
            if (head.val in G) and (prev not in G):
                connected_components += 1
            prev = head.val
            head = head.next

        return connected_components


head = prev = None
for n in [0,1,2,3,4]:
    node = ListNode(n)
    head = head or node
    if prev:
        prev.next = node
    prev = node

print Solution().numComponents(head, [0, 3, 1, 4])
