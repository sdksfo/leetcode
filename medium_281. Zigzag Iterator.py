"""
Requirement:
a) Given two 1d vectors, implement an iterator to return their elements alternatively

Approach:
a) Keep two pointers at the two arrays at 0th position
b) has_next => i < len(A) or j < len(B)
c) next => Return v1 under following conditions a) If v1 ptr is less than v2 ptr and v1 is not exhausted b) v2 is exhausted

"""


class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.i, self.j, self.v1, self.v2 = 0, 0, v1, v2

    def next(self):
        """
        :rtype: int
        """
        if (self.i <= self.j and self.i < len(self.v1)) or (self.j == len(self.v2)):
            self.i += 1
            return self.v1[self.i-1]
        else:
            self.j += 1
            return self.v2[self.j-1]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < len(self.v1) or self.j < len(self.v2)


# Your ZigzagIterator object will be instantiated and called as such:
v1, v2 = [1,5], [3]
i, v = ZigzagIterator(v1, v2), []
while i.hasNext():
	v.append(i.next())
print v
