
"""
Idea is to sum the numbers, from 0 to len(array), Randomly choose a number from 1 to sum. Use
binary search to locate where the number could fall in the array.

e.g [1,2,3,4,4,5] becomes [1, 3, 6, 10, 14, 19]. So select a weight from 1 to 19. And then binary search the array
to see where the weight could lie.
"""

import random

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.weights, total = [], 0
        for i in w:
        	total += i
        	self.weights.append(total)

    def search(self, target, i, j):
    	"""Does a binary search for the randomnumber"""
    	if i > j:
    		return i
    	mid = (i+j)/2
    	if self.weights[mid] == target:
    		return mid
    	if target > self.weights[mid]:
    		return self.search(target, mid+1, j)
    	else:
    		return self.search(target, i, mid-1)

    def pickIndex(self):
        """
        :rtype: int
        """
        randnum = random.randint(1, self.weights[-1])
        return self.search(randnum, 0, len(self.weights)-1)
