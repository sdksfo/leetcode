
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i , j = 1, n+1

        while i < j:
        	mid = i + (j-i)/2

        	if isBadVersion(mid) and not isBadVersion(mid-1):
        		return mid
        	if isBadVersion(mid):
        		j = mid
        	else:
        		i = mid + 1

        return i
