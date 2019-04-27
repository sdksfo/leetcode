

import collections

class FreqStack(object):

    def __init__(self):
		self.element_frequency = collections.defaultdict(int)
		self.frequency_element = collections.defaultdict(list)
		self.max_frequency = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.element_frequency[x] += 1
        self.max_frequency = max(self.max_frequency, self.element_frequency[x])
        self.frequency_element[self.element_frequency[x]].append(x)

    def pop(self):
        """
        :rtype: int
        """
        element = self.frequency_element[self.max_frequency].pop()
        self.element_frequency[element] -= 1
        if not self.frequency_element[self.max_frequency]:
        	self.max_frequency -= 1
        return element

# Your FreqStack object will be instantiated and called as such:
obj = FreqStack()
for x in [5,7,5,7,7,7,4]:
	obj.push(x)
print obj.pop()
print obj.pop()
print obj.pop()
print obj.pop()
print obj.pop()
print obj.pop()
print obj.pop()