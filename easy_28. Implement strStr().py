
# Approach 1: Simple python solution

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return needle in haystack

# Approach 2: Checking every index

class Solution(object):
    def strStr(self, h, n):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in xrange(len(h)-len(n)+1):
        	if h[i:(i+len(n))] == n:
        		return i
        return -1
