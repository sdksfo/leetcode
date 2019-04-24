"""
Push happens on the pushstack and popstack helps with pop and peek. Fill the popstack if it goes empty.
"""

class MyQueue(object):

    def __init__(self):
        self.pushstack, self.popstack = [], []

    def push(self, x):
        self.pushstack.append(x)

    def pop(self):
    	self.move()
    	return self.popstack.pop()

    def peek(self):
    	self.move()
    	return self.popstack[-1]

    def empty(self):
    	return not self.pushstack and not self.popstack

    def move(self):
        if not self.popstack:
            while self.pushstack:
                self.popstack.append(self.pushstack.pop())
