

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s != t:
	        if len(s) == len(t):
	        	for i in xrange(len(s)):
	        		if s[:i] + s[i+1:] == t[:i] + t[i+1:]:
	        			return True
	        elif len(s) > len(t) and len(s) - len(t) == 1:
	        	for i in xrange(len(s)):
	        		if s[:i] + s[i+1:] == t:
	        			return True
	        elif len(t) > len(s) and len(t) - len(s) == 1:
	        	for i in xrange(len(t)):
	        		if t[:i] + t[i+1:] == s:
	        			return True
        return False

print Solution().isOneEditDistance('ab', 'ce')
