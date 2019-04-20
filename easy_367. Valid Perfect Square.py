"""
Check from 1 through num/2 to see if any of them could be squared to get your num.
"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i, j = 1, (num/2) + 2

        while i < j:
        	m = i + (j-i)/2
        	if m * m == num:
        		return True
        	if m * m < num:
        		i = m + 1
        	else:
        		j = m

        return False

for l in xrange(1, 65):
	print l, Solution().isPerfectSquare(l)
