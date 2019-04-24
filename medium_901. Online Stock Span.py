
"""
First solved by similar to the daily temperatures problem. The second approach is a modified version by just storing the counts.
"""

class StockSpanner(object):

    def __init__(self):
    	self.stack = []
    	self.ctr = 0

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.ctr += 1
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        self.stack.append([price, self.ctr])
        if len(self.stack) == 1: return self.ctr
        next_best, next_idx = self.stack[-2]
        return (self.ctr - next_idx + 1) if next_best <= price else self.ctr - next_idx



class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        count = 1
        while self.stack and price >= self.stack[-1][0]:
            count += self.stack.pop()[1]
        self.stack.append([price, count])
        return count

# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()

for i in [20,20,30,40,10,5]:
    print i, obj.next(i)