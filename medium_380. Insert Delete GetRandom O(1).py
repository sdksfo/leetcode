# Explanation

# Build a set with an underlying array implementation (also use dictionary for faster lookups).
# We will use this time complexity matrix to devise our algorithm: https://wiki.python.org/moin/TimeComplexity

# INSERT operation:

# Append to the end of the array and store the idx of it in a dictionary.

# REMOVE operation:

# Find the idx of the element looking up dictionary, swap the idx of the element with the last idx in array and pop the last_idx, update the dictionary
# with new references

# RANDOM operation:

# We can use `random` library to pick a random element from array. random.randint picks anything from 0 thru' len(array)-1

import random

class RandomizedSet(object):

    def __init__(self):
        self.array , self.dict = [], {}

    def insert(self, val):
        if val not in self.dict: # dict getitem - O(1)
        	self.array.append(val) # array append - O(1)
        	self.dict[val] = len(self.array) - 1 # dict putitem - O(1)
        	return True
        return False

    def remove(self, val):
        if val in self.dict: # dict getitem - O(1)
        	idx = self.dict[val] # dict getitem - O(1)
        	self.array[idx] = self.array[-1] # array put - O(1)
        	self.dict[self.array[-1]] = idx # dict putitem - O(1)
        	del self.dict[val] # dict delete O(1)
        	self.array.pop() # array pop O(1)
        	return True
        return False

    def getRandom(self):
        rand_idx = random.randint(0, len(self.array)-1) # array get length - O(1)
        return self.array[rand_idx] # array get - O(1)


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print obj.insert(1)
print obj.remove(2)
print obj.insert(2)
print obj.getRandom()
print obj.remove(1)
print obj.insert(2)
print obj.getRandom()
