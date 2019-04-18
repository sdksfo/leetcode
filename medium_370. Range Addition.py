"""
a) Set the first number in the range as '+inc' and the number after last as '-inc'
b) Run through the array and update each element based on a running total. Once the range is reached,
the total automatically gets reduced by '-inc' preventing an incorrect update.

Time O(k+n) Space O(n)
"""

class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        output = [0] * (length+1)

        for start, end, inc in updates:
        	output[start] += inc
        	output[end+1] -= inc

        total = 0

        for i in xrange(len(output)):
        	total += output[i]
        	output[i] = total

        output.pop()

        return output
