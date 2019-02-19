


class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.queue = []

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.queue) == self.size:
        	self.queue.pop(0)
        self.queue.append(val)
        return sum(self.queue)/float(len(self.queue))


# Your MovingAverage object will be instantiated and called as such:
obj = MovingAverage(3)
print obj.next(1)
print obj.next(10)
print obj.next(3)
print obj.next(5)
