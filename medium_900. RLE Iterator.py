
# So we have a count of a number followed by the number
# We need to maintain two pointers i and j,
# where i points at the count and j points at the number
# when the count at 'i' drops to 0, jump 2 indices to the next
# number. If i == len(array), return -1

class RLEIterator(object):

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.array = A
        self.i = 0

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        for t in xrange(n):
            if self.i == self.leni:
                return -1
            num = self.array[self.j]
            self.array[self.i] -= 1
            if self.array[self.i] == 0:
                while self.i < len(self.array) and self.array[self.i] == 0:
                    self.i += 2
                    self.j += 2
        return num
