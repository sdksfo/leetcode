"""
a) If we compare more than 2 numbers at the same time, repeated numbers could throw the result off i.e i, i-1, i+1
b) So always check if its strictly increasing or decreasing
c) If increasing, set a boolean to True and likewise for decreasing.
d) Where both increasing and decreasing are encountered, return False

Time: O(n) Space O(1)
"""

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        inc = dec = False

        for i in xrange(1, len(A)):
            if A[i] > A[i-1]:
            	inc = True
            if A[i] < A[i-1]:
            	dec = True
            if inc and dec:
            	return False

        return True
